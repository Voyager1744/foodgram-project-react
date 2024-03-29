from api.filters import IngredientSearchFilter, RecipeFilterSet
from api.pagination import CustomPagination
from api.permissions import IsAuthorOrAdminOrReadOnly
from api.serializers import (CreateRecipeSerializer, FavoriteSerializer,
                             FollowListSerializer, FollowSerializer,
                             IngredientSerializer, RecipeSerializer,
                             ShoppingCartSerializer, TagSerializer)
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from recipes.models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                            ShoppingCart, Tag)
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import Follow

from .serializers import UsersSerializer

User = get_user_model()


class UsersViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = CustomPagination

    @action(detail=False)
    def me(self, request):
        user = User.objects.filter(id=request.user.id)
        serializer = UsersSerializer(user, many=True)
        return Response(*serializer.data)

    @action(detail=False)
    def subscriptions(self, request):
        subscriptions_list = self.paginate_queryset(
            User.objects.filter(following__user=request.user)
        )
        serializer = FollowListSerializer(
            subscriptions_list, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)

    @action(methods=['post', 'delete'], detail=True)
    def subscribe(self, request, id):
        if request.method != 'POST':
            subscription = get_object_or_404(
                Follow,
                author=get_object_or_404(User, id=id),
                user=request.user
            )
            self.perform_destroy(subscription)
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = FollowSerializer(
            data={
                'user': request.user.id,
                'author': get_object_or_404(User, id=id).id
            },
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TagViewSet(ModelViewSet):
    """Отображение модели Tag."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientViewSet(ModelViewSet):
    """Отображение модели Ingredient."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)
    pagination_class = None


class RecipeViewSet(ModelViewSet):
    """Отображение модели Recipes."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = CustomPagination
    permission_classes = (
        IsAuthorOrAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilterSet

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeSerializer
        return CreateRecipeSerializer

    @staticmethod
    def post_method_for_actions(request, pk, serializers):
        data = {'user': request.user.id, 'recipe': pk}
        serializer = serializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def delete_method_for_actions(request, pk, model):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        model_instance = get_object_or_404(model, user=user, recipe=recipe)
        model_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def send_message(ingredients):
        shopping_list = 'Купить в магазине:'
        for ingredient in ingredients:
            shopping_list += (
                f"\n{ingredient['ingredient__name']} "
                f"({ingredient['ingredient__measurement_unit']}) - "
                f"{ingredient['amount']}")
        file = 'shopping_list.txt'
        response = HttpResponse(shopping_list, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{file}.txt"'
        return response

    @action(methods=['post', 'delete'], detail=True)
    def shopping_cart(self, request, pk):
        if request.method != 'POST':
            return self.delete_method_for_actions(
                request=request, pk=pk, model=ShoppingCart
            )
        return self.post_method_for_actions(
            request, pk, serializers=ShoppingCartSerializer
        )

    @action(detail=False)
    def download_shopping_cart(self, request):
        ingredients = IngredientInRecipe.objects.filter(
            recipe__shoppingcart__user=request.user
        ).order_by('ingredient__name').values(
            'ingredient__name', 'ingredient__measurement_unit'
        ).annotate(amount=Sum('amount'))
        return self.send_message(ingredients)

    @action(methods=['post', 'delete'], detail=True)
    def favorite(self, request, pk):
        if request.method != 'POST':
            return self.delete_method_for_actions(
                request=request, pk=pk, model=Favorite
            )
        return self.post_method_for_actions(
            request=request, pk=pk, serializers=FavoriteSerializer
        )

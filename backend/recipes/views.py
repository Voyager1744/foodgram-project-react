from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from foodgram.permissions import IsAuthorOrAdminOrReadOnly
from .models import Ingredient, Recipe, Tag
from .serializers import (IngredientSerializer, TagSerializer,
                          RecipeSerializer, CreateRecipeSerializer)


class TagViewSet(ModelViewSet):
    """Отображение модели Tag."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientViewSet(ModelViewSet):
    """Отображение модели Ingredient."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # filter_backends = IngredientFilter  #TODO добавить фильтр
    search_fields = ('^name',)


class RecipeViewSet(ModelViewSet):
    """Отображение модели Recipes."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (
        IsAuthorOrAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeSerializer
        return CreateRecipeSerializer



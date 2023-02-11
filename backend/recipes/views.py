from rest_framework.viewsets import ModelViewSet

from .filters import IngredientFilter
from .models import Ingredient, Recipe, Tag
from .serializers import IngredientSerializer, TagSerializer, RecipeSerializer


class TagViewSet(ModelViewSet):
    """Отображение модели Tag."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


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

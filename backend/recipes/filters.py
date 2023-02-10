from django_filters.rest_framework import FilterSet

from .models import Ingredient


class IngredientFilter(FilterSet):
    """Фильтр по продуктам."""

    class Meta:
        model = Ingredient
        fields = ('name',)

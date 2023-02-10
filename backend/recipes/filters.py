from django_filters.rest_framework import FilterSet, CharFilter

from rest_framework.filters import SearchFilter

from .models import Ingredient


class IngredientFilter(SearchFilter):
    """Фильтр по продуктам."""
    search_param = 'name'
# TODO Добавить фильтр по имени

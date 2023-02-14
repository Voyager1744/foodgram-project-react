from rest_framework import serializers

from .models import Tag, Ingredient, Recipe, IngredientInRecipe
from users.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Tag."""

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug',)


class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Ingredient."""

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


# class IngredientInResipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientInRecipe
#         fields = ('amount',)


class RecipeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Recipe."""
    # tags = TagSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    # ingredients = IngredientInResipeSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            # 'tags',
            'author',
            # 'ingredients',
            'name',
            'image',
            'text',
            'cooking_time',
        )

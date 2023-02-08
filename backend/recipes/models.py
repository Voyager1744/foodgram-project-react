from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

MIN_AMOUNT = 1

User = get_user_model()


class Tag(models.Model):
    """Тег, например: завтрак, обед, ужин."""
    name: str = models.CharField('Название', max_length=200)
    color: str = models.CharField('Цвет Нех-код', max_length=7)
    slug: str = models.SlugField('Slug', max_length=200, unique=True)

    class Meta:
        verbose_name: str = 'Тег'
        verbose_name_plural: str = 'Теги'

    def __str__(self):
        return self.slug


class Ingredient(models.Model):
    """Модель для продуктов."""
    name: str = models.CharField('Название продукта', max_length=200)
    measurement_unit: str = models.CharField(
        'Единица измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class IngredientInRecipe(models.Model):
    """Количество продуктов в рецепте."""
    ingredient: Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredients_in_recipe',
        verbose_name='Продукты в рецепте'
    )
    amount: int = models.IntegerField(
        verbose_name='Количество продукта',
        default=MIN_AMOUNT,
        validators=[MinValueValidator(
            MIN_AMOUNT,
            message=f'Количество продукта должно быть больше {MIN_AMOUNT}')
        ],
    )

    class Meta:
        verbose_name = 'Количество продукта в рецепте'
        verbose_name_plural = 'Количество продуктов в рецепте'
        constraints = (
            models.UniqueConstraint(
                fields=('amount', 'ingredient',),
                name='unique_amount_ingredients'
            )
        )

    def __str__(self):
        return (
            f'{self.ingredient.name} - {self.amount}'
            f' ({self.ingredient.measurement_unit})'
        )


class Recipe(models.Model):
    """Модель для рецепта"""
    pass

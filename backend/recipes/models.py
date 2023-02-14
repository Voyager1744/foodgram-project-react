from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

MIN_AMOUNT = 1
MIN_COOKING_TIME = 1

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
        ordering = ['name']

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    """Модель для рецепта"""
    tags: Tag = models.ManyToManyField(
        Tag,
        verbose_name='Теги'
    )
    author: User = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты рецепта'
    )
    name: str = models.CharField(
        'Название рецепта',
        max_length=200
    )
    image = models.ImageField(
        'Фото',
        blank=True,
        default=None,
        upload_to='recipes/images/'
    )
    text: str = models.TextField(
        'Описание'
    )
    cooking_time: int = models.PositiveSmallIntegerField(
        'Время приготовления, мин',
        validators=[
            MinValueValidator(
                MIN_COOKING_TIME,
                message=f'Время должно быть больше {MIN_COOKING_TIME}'
            )
        ],
        default=MIN_COOKING_TIME
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pk',)

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    """Количество продуктов в рецепте."""
    ingredient: Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Продукты в рецепте'
    )
    amount: int = models.PositiveIntegerField(
        verbose_name='Количество продукта',
        validators=[
            MinValueValidator(
                MIN_AMOUNT,
                message=f'Количество продукта должно быть больше {MIN_AMOUNT}'
            )
        ],
        default=MIN_AMOUNT
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        default_related_name = 'ingredients_in_recipe'
        constraints = (
            models.UniqueConstraint(fields=('recipe', 'ingredient',),
                                    name='unique_amount_ingredients'),)
        verbose_name = 'Количество продукта в рецепте'
        verbose_name_plural = 'Количество продуктов в рецепте'

    def __str__(self):
        return f'{self.recipe}: {self.ingredient} – {self.amount}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='is_favorited',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('user',)
        verbose_name = 'Избранное'
        default_related_name = 'favorites'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_favorites',
            ),
        )


class ShoppingCart(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Корзина'
        constraints = (models.UniqueConstraint(fields=('user', 'recipe'),
                                               name='unique_cart', ),
                       )

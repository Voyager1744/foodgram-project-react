from django.contrib import admin

from .models import Ingredient, IngredientInRecipe, Recipe, ShoppingCart, Tag


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientInRecipe
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug'
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit'
    )
    ordering = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'ingredient',
        'amount'
    )
    list_filter = ('recipe', 'ingredient')


# TODO дописать сортировки

class IngredientsInline(admin.TabularInline):
    model = Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'is_favorited'
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('is_favorited',)
    inlines = (IngredientRecipeInline,)

    def is_favorited(self, obj):
        return obj.is_favorited.all().count()

    is_favorited.short_description = 'Количество в избранном'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')
    list_filter = ('recipe', 'user')
    search_fields = ('user',)

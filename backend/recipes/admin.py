from django.contrib import admin

from .models import Ingredient, IngredientInRecipe, Recipe, Tag


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientInRecipe
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'color',
        'slug',
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    ordering = ('name',)


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ingredient',
        'amount',
        'recipes',
    )
    list_display_links = ('recipes',)


# TODO дописать сортировки


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'is_favorited',
        'name',
        'tag_in_recipe',  # FIXME
        # 'image',
        # 'text',
        'cooking_time',
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = (IngredientRecipeInline,)

    def tag_in_recipe(self, obj):  # FIXME
        return obj.tags.all()

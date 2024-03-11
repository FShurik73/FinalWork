from django.contrib import admin

from recipe_site.models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['title']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cook_steps', 'cook_time', 'image', 'ingredients', 'author']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name']
    save_on_top = True

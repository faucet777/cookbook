from django.contrib import admin
from .models import Product, Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_used')

admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)

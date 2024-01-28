from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Recipe, Product, Ingredient


def add_product_to_recipe(request):
    if request.method == 'GET':

        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)
        ingredient, created = Ingredient.objects.get_or_create(recipe=recipe, product=product)
        ingredient.weight = weight
        ingredient.save()

        return JsonResponse({"recipe_id": recipe_id})


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        ingredients = recipe.ingredient_set.all()

        for ingredient in ingredients:
            ingredient.product.times_used += 1
            ingredient.product.save()

        return JsonResponse({"recipe_id": recipe_id})


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        recipes_without_product = Recipe.objects.exclude(ingredient__product_id=product_id)
        recipes_with_less_than_10g = Recipe.objects.filter(ingredient__product_id=product_id,
                                                           ingredient__weight__lt=10)
        recipes = recipes_without_product | recipes_with_less_than_10g
        context = {'recipes': recipes.distinct()}

        return render(request, 'recipes_without_product.html', context)
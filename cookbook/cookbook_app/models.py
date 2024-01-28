from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    times_used = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='Ingredient')
    def __str__(self):
        return str(self.name)

class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return str(self.product)




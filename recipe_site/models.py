from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория рецепта'
        verbose_name_plural = 'Категории рецептов'

    def __str__(self):
        return f'Category: {self.title}'


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    cook_steps = models.TextField(max_length=2000)
    cook_time = models.IntegerField()
    image = models.ImageField(upload_to='recipe_images', blank=True)
    ingredients = models.TextField(max_length=1000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return (f'Recipe: {self.name}'
                f'description: {self.description}'
                f'cook_steps: {self.cook_steps}'
                f'cook_time: {self.cook_time}'
                f'ingredients: {self.ingredients}'
                f'author: {self.author}')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'




import random

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from recipe_site.forms import CreateRecipe, LoginUserForm, RegForm
from recipe_site.models import Recipe, Category


# Create your views here.

def home(request):
    recipe_list = []
    recipes = Recipe.objects.all()
    if len(recipes) < 5:
        recipe_list.append(recipes)
    else:
        while len(recipe_list) < 5:
            recipe_list.append(random.choice(recipes))

    context = {
        'title': "Главная страница",
        'recipe': recipe_list,
    }
    return render(request, 'recipe_site/index.html', context)

    # return render(request, 'base.html')


def about(request):
    return render(request, 'recipe_site/about.html', {'title': 'О нас'})


class RecipeCreate(CreateView):
    model = Recipe
    form_class = CreateRecipe
    template_name = 'recipe_site/create_recipe.html'


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'title': f'Рецепт: {recipe.name}',
        'recipe': recipe
    }
    return render(request, 'recipe_site/recipe.html', context)


def recipes_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'title': f'Рецепты по категории: {category}',
        'recipe': Recipe.objects.filter(category=category).all()
    }
    return render(request, 'recipe_site/recipe_list.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
    else:
        form = LoginUserForm()
    return render(request, 'recipe_site/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'recipe_site/login.html'


class CreateUser(CreateView):
    model = User
    form_class = RegForm
    template_name = 'recipe_site/registration.html'

from django.urls import path

from . import views

from .views import CreateUser, RecipeCreate

#
# app_name = "users"

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('category/<int:category_id>', views.recipes_by_category, name='Recipe by category'),
    path('recipe/<int:recipe_id>', views.recipe, name='Recipe'),
    # path('search/', SearchRecipe.as_view(), name='search'),
    path('add/', RecipeCreate.as_view(), name='Create recipe'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('signup/', CreateUser.as_view(), name='reg'),
]

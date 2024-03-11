from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Recipe, Category


class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cook_steps', 'cook_time', 'image', 'ingredients', 'author', 'category']
        classes = []


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', widget=forms.CharField())


class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',]


class UploadPhotoForm(forms.Form):
    image = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form_user_personal_account_upload_user_photo'}))


class Authorization(forms.Form):
    email = forms.EmailField(required=True, label='Электронная почта', widget=forms.EmailInput(
            attrs={'class': 'form_user_log_in_personal_account', 'placeholder': 'Адрес электронной почты'}))
    password = forms.CharField(required=True, label="Пароль", widget=forms.PasswordInput(
        attrs={'class': 'form_user_log_in_personal_account', 'placeholder': 'Пароль'}))


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

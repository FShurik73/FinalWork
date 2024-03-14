from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Recipe, Category


class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cook_steps', 'cook_time', 'image', 'ingredients', 'author', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите название блюда',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите описание блюда'
            }),
            'cook_steps': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите как готовится блюдо'
            }),
            'cook_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите время приготовления блюда'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ингредиенты'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
        classes = []


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', widget=forms.CharField())


class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите электронную почту'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
        }


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

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForms(UserCreationForm):
    username = forms.CharField(required=True, label='Логин')
    first_name = forms.CharField(required=True, label='Имя')
    last_name = forms.CharField(required=True, label='Фамилия')
    email = forms.EmailField(required=True, label='e-mail')
    password1 = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, label='Подтвердить пароль', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput())
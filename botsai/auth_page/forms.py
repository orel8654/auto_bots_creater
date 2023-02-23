from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForms(UserCreationForm):
    username = forms.CharField(required=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-reg'}))
    first_name = forms.CharField(required=True, label='Имя', widget=forms.TextInput(attrs={'class': 'form-reg'}))
    last_name = forms.CharField(required=True, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-reg'}))
    email = forms.EmailField(required=True, label='e-mail', widget=forms.TextInput(attrs={'class': 'form-reg'}))
    password1 = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-reg'}))
    password2 = forms.CharField(required=True, label='Подтвердить пароль', widget=forms.PasswordInput(attrs={'class': 'form-reg'}))
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
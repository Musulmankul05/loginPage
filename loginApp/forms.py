from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UserModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = UserModel
        fields = ("username", "password")


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = UserModel
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2'
        ]

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Enter username'
    }))
  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Enter your email'
    }))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Enter password'
    }))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat password'
    }))


class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Enter username'
    }))
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Enter password'
    }))


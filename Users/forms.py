from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class UserForm(UserCreationForm):
	class Meta:
		model= User
		fields=('email','phone_number','password1','password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
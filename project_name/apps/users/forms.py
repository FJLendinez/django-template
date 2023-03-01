from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpRequest


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")

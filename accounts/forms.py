#Sign up Form using inbuilt django form

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm) : 
    """Sign Up Form Student and Instructor"""
    roles = forms.ChoiceField(choices = User.ROLE_CHOICES)

    class Meta : 
        model = User
        fields = ('username', 'email', 'roles', 'password1', 'password2')

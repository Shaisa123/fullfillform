from django import forms
from django.db import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

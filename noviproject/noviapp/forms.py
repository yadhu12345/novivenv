from dataclasses import fields
from django import forms
from .models import *
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id':'username','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id':'password','placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ('username','password')
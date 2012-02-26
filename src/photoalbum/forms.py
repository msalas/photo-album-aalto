from django import forms
from django.forms import widgets, ModelForm, ClearableFileInput
from models import *

class LoginForm(forms.Form):
    username = forms.CharField( max_length=16 )
    password = forms.CharField( max_length=16, widget=forms.PasswordInput )
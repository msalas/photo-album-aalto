### forms.py
### This module contains all the form definitions for Webshop.
### (c) 2011 The Webshop Team.

### necessary Django modules ###
from django import forms
from django.forms import widgets
from models import *

##
##
# Form for user registration.
class RegistrationForm(forms.Form):
    firstname      = forms.CharField(max_length=16 )
    surname        = forms.CharField(max_length=16 )
    username       = forms.CharField(max_length=16 )
    password       = forms.CharField(widget=forms.PasswordInput)
    email          = forms.CharField(max_length=32)

#Form for login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=16 )
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)

##
# Form for user profile.
class ProfileForm(forms.Form):
    firstname       = forms.CharField(max_length=16)
    surname         = forms.CharField(max_length=16)
    username        = forms.CharField(max_length=16)
    password        = forms.CharField(widget=forms.PasswordInput)
    email           = forms.CharField(max_length=32)

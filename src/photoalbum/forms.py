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

class AlbumForm(forms.Form):
    album_name       = forms.CharField(max_length=16)
    public           = forms.BooleanField(required=False)
    
class PageForm(forms.Form):
    album_id           = forms.IntegerField()
    layout           = forms.ChoiceField(choices=[("0", "Layout 1"),
                                         ("1", "Layout 2"),
                                         ("2", "Layout 3")],
                                widget=forms.Select)
    
class UploadImageForm(forms.Form):
    caption            = forms.CharField(max_length=50)
    page_id            = forms.IntegerField()
    picture            = forms.FileField()
    album_id           = forms.IntegerField()
#    path                = models.FilePathField()


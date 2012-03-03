from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from photoalbum.models import *
#from django import forms
from photoalbum.forms import *

class LoginForm(forms.Form):
    username = forms.CharField( max_length=16 )
    password = forms.CharField( max_length=16, widget=forms.PasswordInput )
	
##
# Render the home page. 
def main(request):
    t = loader.get_template('main.html')

    context = RequestContext(request, {
    'user'  : request.user,
    }) 
    # if the user is authenticated
    if request.user.is_authenticated():
        user = request.user
        template = loader.get_template('myalbums')
        albums = Album.objects.filter(owner__id__exact=user.id)
        public_albums = Album.objects.filter(visible=True).filter(owner__id__exact=user.id)
        if len(albums) == 0:           
            context.update({'public_albums': public_albums})
        else:
            context.update({'album': albums})
            context.update({'public_albums': public_albums})
            
    else:
        login_form = LoginForm()
        context.update({'login_form': login_form})
        
    # render the home page
    context.update(csrf(request))
    return HttpResponse(t.render(context))
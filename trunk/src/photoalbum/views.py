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


##
# Render the home page. 
def main(request):
    t = loader.get_template('main.html')
    
    albums = Album.objects.filter(owner__id__exact=0)
    context = RequestContext(request, {
    'user'  : request.user,
    'album' : albums,
    }) 
    # if the user is authenticated
    if request.user.is_authenticated():
        user = request.user
        template = loader.get_template('myalbums')
        public_albums = Album.objects.filter(visible=True).filter(owner__id__exact=0)
        context.update({'album': albums})
    else:
        login_form = LoginForm()
        context.update({'login_form': login_form})
        
    # render the home page
    context.update(csrf(request))
    return HttpResponse(t.render(context))
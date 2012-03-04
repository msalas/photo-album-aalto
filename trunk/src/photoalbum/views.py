from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from albums.models import *
from settings import *
from django import forms
from photoalbum.forms import *
from photoalbum.login import *
from photoalbum.utils import *
import flickrapi
#from django.contrib.auth import logout as auth_logout
#from django.contrib.auth.decorators import login_required
#from django.contrib.messages.api import get_messages
from facebook import *

# Render the home page.
def main(request):
    t = loader.get_template('main.html')
#    facebook_profile = request.user.get_profile().get_facebook_profile()

    context = RequestContext(request, {
    'user'  : request.user,
#    'facebook_profile': facebook_profile,
    }) 
    # if the user is authenticated
    if request.user.is_authenticated():
        user = request.user
        
        album_list = Album.objects.filter(owner__id__exact=request.user.id) # not sure about the order_by id is correct or not.. but didnt complain
        return render_to_response('albums/index.html', {'user'  : request.user, 'album_list': album_list}, context_instance=RequestContext(request))
 #       template = loader.get_template('createAlbum.html')
 #       albums = Album.objects.filter(owner__id__exact=user.id)
 #       public_albums = Album.objects.filter(visible=True).filter(owner__id__exact=user.id)
 #       if len(albums) == 0:           
  #          context.update({'public_albums': public_albums})
 #       else:
 #           context.update({'album': albums})
 #           context.update({'public_albums': public_albums})
            
    else:
        login_form = LoginForm()
        context.update({'login_form': login_form})
        
    # render the home page
    context.update(csrf(request))
    return HttpResponse(t.render(context))


def profile(request):
    return render_to_response('profile.html')


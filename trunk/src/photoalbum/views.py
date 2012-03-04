from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from photoalbum.models import *
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
        template = loader.get_template('createAlbum.html')
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


def createAlbum(request, **kwargs):
    t = loader.get_template('createAlbum.html')
    album_form = AlbumForm(); 

    context = RequestContext(request, {
    'user'  : request.user,
    }) 
    
    if request.user.is_authenticated():
        u = User.objects.get(id=request.user.id)
        
        if request.method == 'POST':
            form = AlbumForm(request.POST)
            if form.is_valid():
                # get the clean data from the POST
                album_name = form.cleaned_data['album_name']
                layout = form.cleaned_data['layout']
                public = form.cleaned_data['public']
                
                album  = Album.objects.create(owner_id = u.id)
                album.album_name = album_name
                album.layout = layout
                album.public = public
                album.save()
                
                uploadImageForm = UploadImageForm()
                t = loader.get_template('addPhoto.html')
                context = RequestContext(request, { 
 #                   'album'        : albums,
                    'album_id'          : album.id,
                    'uploadImageForm'   : uploadImageForm,
                })
        else:
            context = RequestContext(request, { 
 #           'album'   : albums,
            'album_form'   : album_form,
        })
    else:
        return HttpResponseRedirect('/')
        
    # render the home page
    context.update(csrf(request))
    return HttpResponse(t.render(context))

    
def addPhoto(request, **kwargs):
    t = loader.get_template('addPhoto.html')
    upload_image_form = UploadImageForm(); 

    context = RequestContext(request, {
    'user'  : request.user,
    }) 
    
    if request.user.is_authenticated():
        u = User.objects.get(id=request.user.id)
        
        if request.method == 'POST':
            form = UploadImageForm(request.POST, request.FILES)
            if form.is_valid():
                # get the clean data from the POST
                album_id = form.cleaned_data['album_id']
                print album_id
                caption = form.cleaned_data['caption']
                picture = request.FILES.get('picture')
                handleUploadedPic(str(u.id), picture, album_id)
                
                print "creating image..."
                image = Image.objects.create()
                print "album_id is:"
                print image.album_id
                image.album_id = album_id
                print image.album_id
                image.picture = picture
                image.save()
                print image.album_id
                
                sentence = Sentence.objects.create()
                sentence.description = caption
                sentence.save() 
                
                return HttpResponseRedirect('/')
            else:
                print form.errors
        else:
            context = RequestContext(request, { 
 #           'album'   : albums,
            'uploadImageForm'   : upload_image_form,
        })
    else:
        print "user is not authenticated"
        return HttpResponseRedirect('/')
        
    # render the home page
    context.update(csrf(request))
    print "rendering response in the end..."
    return HttpResponse(t.render(context))
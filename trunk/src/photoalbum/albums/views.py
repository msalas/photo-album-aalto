from django.shortcuts import render_to_response
#from django.http import HttpResponse
from photoalbum.models import *
from django import forms
from photoalbum.forms import *
from photoalbum.login import *
from photoalbum.utils import *
from photoalbum.settings import MEDIA_ROOT

def index(request):
    #return HttpResponse("Hello, world. You're at the albums index.")
    album_list = Album.objects.filter(owner__id__exact=request.user.id) # not sure about the order_by id is correct or not.. but didnt complain
    return render_to_response('albums/index.html', {'user'  : request.user, 'album_list': album_list}, context_instance=RequestContext(request))

def viewAlbum(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    page_list = Page.objects.filter(album_id=album_id)
    if len(page_list) == 0:
        return render_to_response('albums/page.html', {'user'  : request.user, 'page_list': page_list, 'album': album}, context_instance=RequestContext(request))
    else:
        image_list = Image.objects.filter(album_id=album_id).filter(page_id=page_list[0].id)
#    sentence_list = Sentence.objects.filter(image_id=album_id)
        return render_to_response('albums/page.html', {'user'  : request.user, 'page_list': page_list, 'album': album, 'image_list': image_list}, context_instance=RequestContext(request))

def viewImage(request, image_id):
    image = Image.objects.get(id=image_id)
    sentence = Sentence.objects.get(image_id=image_id)
    return render_to_response('albums/photo.html', {'user'  : request.user, 'image': image, 'sentence': sentence}, context_instance=RequestContext(request))

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
                public = form.cleaned_data['public']
                
                album  = Album.objects.create(owner_id=u.id)
                album.title = album_name
                album.public = public
                album.save()
                
                pageForm = PageForm()
                t = loader.get_template('addPage.html')
                context = RequestContext(request, { 
                    'user'  : request.user,
                    'album_id'          : album.id,
                    'page_form'          : pageForm,
                })
        else:
            context = RequestContext(request, { 
 #           'album'   : albums,
            'album_form'   : album_form,
            'user'  : request.user,
        })
    else:
        return HttpResponseRedirect('/')
        
    # render the home page
    context.update(csrf(request))
    return HttpResponse(t.render(context))

    
def addPage(request, **kwargs):
    t = loader.get_template('addPage.html')
    page_form = PageForm(); 

    context = RequestContext(request, {
    'user'  : request.user,
    }) 
    
    if request.user.is_authenticated():
        u = User.objects.get(id=request.user.id)
        
        if request.method == 'POST':
            form = PageForm(request.POST)
            if form.is_valid():
                # get the clean data from the POST
                album_id = form.cleaned_data['album_id']
                layout = form.cleaned_data['layout']
                
                page = Page.objects.create()
                page.album_id = album_id
                page.layout_id = layout
                page.save()
                
                uploadImageForm = UploadImageForm()
                t = loader.get_template('addPhoto.html')
                context = RequestContext(request, { 
                    'user'  : request.user,
                    'album_id'          : album_id,
                    'page_id'           : page.id,
                    'uploadImageForm'   : uploadImageForm,
                })
            else:
                print form.errors
        else:
            context = RequestContext(request, { 
            'user'  : request.user,
            'page_form'   : page_form,
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
                albumId = form.cleaned_data['album_id']
                caption = form.cleaned_data['caption']
                pageId = form.cleaned_data['page_id']
                picture = request.FILES.get('picture')
                filename = handleUploadedPic(str(u.id), picture, albumId)
                print "filename:"
                print filename
                
                image = Image.objects.create()
                image.album_id = albumId
                image.page_id = pageId
                image.picture = filename
                image.save()
                
                sentence = Sentence.objects.create()
                sentence.description = caption
                sentence.image_id = image.id
                sentence.save() 
                
                t = loader.get_template('profile.html')
                context = RequestContext(request, { 
                    'user'  : request.user,
                })
            else:
                print form.errors
        else:
            context = RequestContext(request, { 
 #           'album'   : albums,
            'uploadImageForm'   : upload_image_form,
        })
    else:
        return HttpResponseRedirect('/')
        
    # render the home page
    context.update(csrf(request))
    return HttpResponse(t.render(context))
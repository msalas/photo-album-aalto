from django.shortcuts import render_to_response
#from django.http import HttpResponse
from photoalbum.albums.models import Album

def index(request):
    #return HttpResponse("Hello, world. You're at the albums index.")
    album_list = Album.objects.all().order_by('-id') # not sure about the order_by id is correct or not.. but didnt complain
    return render_to_response('albums/index.html', {'album_list': album_list})


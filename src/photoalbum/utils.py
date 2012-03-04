### utils.py
### Misc utilities to be used in Webshop.
### (c) 2011 The Webshop Team

### necessary libraries ###
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from photoalbum.settings import MEDIA_ROOT
import flickrapi

##
# Handle an uploaded file.
#
# This function does not only save a file but also do other checks (e.g. picture
# size and resolution). TODO: this is not yet implemented!
#
# @param d Directory where to store the picture.
# @param f File to be handled.
# @param n Name of the file.
def handleUploadedPic(d, f, n):
    # if no file uploaded, don't change the picture
    if f is None:
        return
    
    filename =  d + "." + str(n) + '.png'
    # if a file is provided, then save it where it belongs
    fo = open('%s/%s' % (MEDIA_ROOT, filename), 'wb')
#    fo = open('static/uploads/' + d + '/' + str(n), 'wb+')
    for chunk in f.chunks():
        fo.write(chunk)
    fo.close()
    return filename

  
###Flickr stuff
#def photos_search(user_id='', auth=False,  tags='', tag_mode='', text='',\
#                  min_upload_date='', max_upload_date='',\
#                  min_taken_date='', max_taken_date='', \
#                  license='', per_page='', page='', sort=''):
# 
#
#    method = 'flickr.photos.search'
#
#    data = _doget(method, auth=auth, user_id=user_id, tags=tags, text=text,\
#                  min_upload_date=min_upload_date,\
#                  max_upload_date=max_upload_date, \
#                  min_taken_date=min_taken_date, \
#                  max_taken_date=max_taken_date, \
#                  license=license, per_page=per_page,\
#                  page=page, sort=sort)
#    photos = []
#    if isinstance(data.rsp.photos.photo, list):
#        for photo in data.rsp.photos.ph
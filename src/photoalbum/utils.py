### utils.py
### Misc utilities to be used in Webshop.
### (c) 2011 The Webshop Team

### necessary libraries ###
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from photoalbum.settings import MEDIA_ROOT


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

    # if a file is provided, then save it where it belongs
    fo = open('%s/%s' % (MEDIA_ROOT, d + "." + str(n)), 'wb')
#    fo = open('static/uploads/' + d + '/' + str(n), 'wb+')
    for chunk in f.chunks():
        fo.write(chunk)
    fo.close()

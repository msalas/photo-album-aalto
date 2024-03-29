# Uncomment the next two lines to enable the admin:
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()
#from photoalbum.views import xd_receiver

urlpatterns = patterns('',

#    # Examples:
#    # url(r'^$', 'photoalbum.views.home', name='home'),
#    # url(r'^photoalbum/', include('photoalbum.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^signup$', 'photoalbum.views.signup'),
    (r'^signin$', 'photoalbum.views.signin'),
    (r'^signout$', 'photoalbum.views.signout'),
#    (r'^editProfile$', 'photoalbum.views.editProfile'),

    (r'^facebook/login$', 'facebook.views.login'),
    (r'^facebook/authentication_callback$', 'facebook.views.authentication_callback'),
    (r'^logout$', 'django.contrib.auth.views.logout'),

    
#    (r'^myadmin$', 'photoalbum.views.myadmin'),
	 (r'^$', 'photoalbum.views.main'),   
 
    (r'^profile$', 'photoalbum.views.profile'),
   
    (r'^albums$','albums.views.index'),
    (r'^albums/(?P<album_id>\d+)/$', 'albums.views.viewAlbum'),
    (r'^albums/(?P<image_id>\d+)$', 'albums.views.viewImage'),
    (r'^createAlbum$', 'albums.views.createAlbum'),
    (r'^addPhoto$', 'albums.views.addPhoto'),
    (r'^addPage$', 'albums.views.addPage'),
    
)

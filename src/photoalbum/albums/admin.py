from django.contrib import admin
from photoalbum.albums.models import Album, Page

#class AlbumAdmin(admin.ModelAdmin):
#search_fields = ["title"]
#list_display = ["title", "user"]

#class PageAdmin(admin.ModelAdmin):
#search_fields = ["title"]
#list_display = ["title"]
#list_filer = ["albums"]

#class ImageAdmin(admin.ModelAdmin):
#search_fields = ["title"]
#list_display = ["title", "size", "image", "thumbnail", "date_created"]
#list_filer = ["pages"]


admin.site.register(Album)
admin.site.register(Page)
#admin.site.register(Image, ImageAdmin)
from django.db import models


class Album(models.Model):
    title       = models.CharField(max_length=32, blank = False)
    #cover_id    = models.CharField(max_length=10) # whats this?
    visible     = models.BooleanField(default=True)
    owner       = models.CharField(max_length=32) #models.ForeignKey(UserProfile)
    #front_page  = models.FilePathField() # whats this?
    
    def __unicode__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=75)
    album = models.ForeignKey(Album)
    
    def __unicode__(self):
        return self.title

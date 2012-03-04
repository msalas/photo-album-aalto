from django.db import models

##
# Model: Album
#
# id          implicit ID field (automatically generated)
# name        name of the category
# visible    


class Album(models.Model):
    title       = models.CharField(max_length=32, blank = False)
    cover_id    = models.CharField(max_length=10) # This is supposed to be the cover picture of the album
    visible     = models.BooleanField(default=True)
    owner       = models.CharField(max_length=32) #models.ForeignKey(UserProfile)
    #front_page  = models.FilePathField() # whats this?
    
    def __unicode__(self):
        return self.title
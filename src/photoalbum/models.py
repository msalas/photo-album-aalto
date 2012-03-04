### Models module
### (c) Group 013



### necessary libraries ###
from django.db import models
#from django.utils.datetime_safe import datetime
#from django.template.defaultfilters import default
from django.contrib.admin.models import User
#from django.db.models.signals import post_save
#import math, md5


##
# Model: UserProfile
# 
# Uses the built in django.contrib.auth to manage users and authentication.
# Adds fields to manage the postal information of the user.
#
# user             references the built in user class of django.
# picture          path to the static file containing the user profile's picture

class UserProfile( models.Model ):
    user           = models.ForeignKey(User, unique=True)
    picture        = models.CharField(max_length=256)
    
    def get_user(self):
        return self.__user

    def set_user(self, value):
        self.__user = value
   
    def __unicode__(self):
        return self.user.name

##
# Activates the create_user_profile handler when a new user is saved.
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


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
    owner       = models.ForeignKey(UserProfile)
    #front_page  = models.FilePathField() # whats this?
    
    def __unicode__(self):
        return self.title

class Page(models.Model):
#    title = models.CharField(max_length=75)
    layout      = models.IntegerField(null=True) 
    album_id       = models.IntegerField(null=True)
    
    def __unicode__(self):
        return self.title
    
     
##
# Model: Image
#
#
class Image(models.Model):
#    filename            = models.CharField(max_length=50)
#    picture             = models.ImageField(upload_to='uploads')
    picture             = models.CharField(max_length=100)
    album_id            = models.IntegerField(null=True)
    page_id             = models.IntegerField(null=True)
#    path                = models.FilePathField()
    
    def savePicture(self):
        self.save()
      
    def __unicode__(self):
        return self.name


##
# Model: Sentence

# 
class Sentence(models.Model):
    description     = models.CharField(max_length=100)
    image_id        = models.IntegerField(null=True)
    font            = models.CharField(max_length=20)
    size            = models.IntegerField(null = True)
    color           = models.CharField(max_length=7)
    
    
    def saveSentence(self):
    #todo
        self.save()
        
    def __unicode__(self):
        return self.name



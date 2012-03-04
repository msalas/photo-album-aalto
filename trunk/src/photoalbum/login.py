### login.py
### This module contains user registration and session functionalities.
### The Photo Album Team

### necessary libraries ###
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.template import Context, RequestContext, loader
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
#from myadmin import *
import os.path
from photoalbum.models import *
from forms import *
import datetime, hashlib, os
from photoalbum.forms import *

#Defines is_auth
def is_auth(request):
    if request.user.is_authenticated():
        return True
    else:
        return False
##
# Render a simple registration form (sign up)
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)  
        
        errors = False
        name_error = ""
        mail_error = ""
        check_email = ""
        message_error = ""
        
        # check if the user already exists in the database
        try:
            check_username = User.objects.get(username=request.POST.get('username'))
            errors = True
            name_error = "This username is already registered"
            print "name error"
        except:
            check_username = None
            
        try:
            check_email = User.objects.get(email=request.POST.get('email'))
            errors = True
            mail_error = "This email is already registered"
            print "mail_error"
            
        except:
            check_email = None

        # if the username or email already exists, go back to the sign-up
        # form and remember the entered data
        if errors:
            t = loader.get_template('signup.html')
            login_form = LoginForm()
            print message_error
            context = RequestContext(request, {
                'username'       : request.POST.get('username'),
                'firstname'      : request.POST.get('firstname'),
                'surname'        : request.POST.get('surname'),
                'email'          : request.POST.get('email'),
                'password'       : request.POST.get('password'),
                'user_exists'    : True,
                'form'           : form,
                'login_form'     : login_form,
                'name_error'     : name_error,
                'mail_error'     : mail_error,
                'check_email'    : check_email,
                'message_error'  : message_error,
                })
            context.update(csrf(request))
            return HttpResponse(t.render(context))
            
        else:
            # save all the data from the POST into the database
            u  = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('password')
            )           
            up = UserProfile.objects.create(user_id=u.id)
            u.first_name = request.POST.get('firstname')
            u.last_name  = request.POST.get('surname')
            u.save()
            up.save()   
            
               
            t = loader.get_template('signin.html')
            login_form = LoginForm()
              
            # redirect the user to the login page with a welcome message
            context = RequestContext(request, {
                'username'      : request.POST.get('username'),
#             'album'         : albums,
                'login_form'    : login_form,
                'registered'    : True,
            })
            context.update(csrf(request))
            return HttpResponse(t.render(context))
    
    else:
        t = loader.get_template('signup.html')
        form = RegistrationForm()
        login_form = LoginForm()
#        album = album.objects.all()
        context = RequestContext(request,
        {
            'form'       : form,
#            'album'      : albums,
            'login_form' : login_form,
        })
        return HttpResponse(t.render(context))


##
# Render a simple login form (sign in)
def signin(request):
    t = loader.get_template('signin.html')
#    album = album.objects.all()
    login_form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # get the clean data from the POST
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # try to validate the user against the DB
            print'print this'
            user = authenticate(username=username, password=password)
            if user is not None:
                # login the user and redirect to the front page
                login(request, user)
                return HttpResponseRedirect('profile.html')
            else:
                context = RequestContext(request, { 
 #                   'album'        : albums,
                    'login_form'   : login_form,
                    'login_failed' : True,
                })
    else:
        # if the input values are not correct, or direct access to this page    
        context = RequestContext(request, { 
 #           'album'   : albums,
            'login_form'   : login_form,
        })

    # render the login page.
    return HttpResponse(t.render(context))


##
# Close the session for an user and go to the front page.
def signout(request):
    if is_auth(request):
        logout(request)
        return HttpResponseRedirect('/')  


##
# Render the user profile page.
def editProfile(request):
    if is_auth(request):
        t = loader.get_template('profile.html')
        form = ProfileForm(request.POST, request.FILES)

        # obtain the data from the user and display his/her profile
        u = User.objects.get(id=request.user.id)

        # set the rest of the data
        context = RequestContext(request, {
            'username'         : u.username,
            'firstname'        : u.first_name,
            'surname'          : u.last_name,
            'email'            : u.email,
#            'album'            : albums,
#            'form'             : form,
       })
        context.update(csrf(request))
        return HttpResponse(t.render(context))


##
# Save the user's profile.
#def saveProfile(request):
#    if is_auth(request) and request.method == 'POST':
#        t = loader.get_template('profile.html')

        # save all the data from the POST into the database
#        up = UserProfile.objects.get(user=request.user.id)
#        u = User.objects.get(id=request.user.id)
#        u.first_name = request.POST.get('firstname')
#        u.last_name  = request.POST.get('surname')

        # commit to the database
#        u.save()
#        up.save()

        # display profile again
#        form = ProfileForm(request.POST, request.FILES)
#        context = RequestContext(request, {
#            'username'       : u.username,
#            'firstname'      : u.first_name,
#            'surname'        : u.last_name,
#            'email'          : u.email,
#            'form'           : form,
#            'saved'          : True,
#        })

        # redirect the user to the home page (already logged-in)
#        context.update(csrf(request))
#        return HttpResponse(t.render(context))
#from django.template.loader import get_template
#from django.template import Context
from django.template import RequestContext, loader
from django.core.context_processors import csrf
#from django.shortcuts import get_object_or_404
#from django.contrib.auth.models import User
from django.http import HttpResponse
#from django.http import import HttpResponseRedirect
#from photoalbum.models import *
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField( max_length=16 )
    password = forms.CharField( max_length=16, widget=forms.PasswordInput )


def main(request):
    t = loader.get_template('main.html')
 
   
    # load the categories and the products ordered by rating
#  categories = Category.objects.all()
#  best_products = Product.objects.filter(stock_count__gt=0).order_by('-average_rating')[:10]
    
    context = RequestContext(request, {
  #      'categories'  : categories,
  #      'products'    : best_products,
    })
    
    # if the user is authenticated, then send info about the card in the request
#if request.user.is_authenticated():
#        albums = Album.objects.filter(owner=request.user.username)
#covers = Image.objects.
#        context.update({'albums': albums})
    login_form = LoginForm()
    context.update({'login_form': login_form})
    
    # if show-as-icons option, then send this option to the template
    if request.GET.get('l') == 'icons':
        context.update({'icons': 'OK'})
        
    # render the home page
    context.update(csrf(request))
    return HttpResponse(t.render(context))
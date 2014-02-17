
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.core.exceptions import *
import twitter

from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET



def get_connection():
    api = None
    error = None  	
    try:
        api = twitter.Api(consumer_key = CONSUMER_KEY,
                          consumer_secret = CONSUMER_SECRET,
                          access_token_key = ACCESS_TOKEN_KEY,
                          access_token_secret = ACCESS_TOKEN_SECRET)
    except NameError:
        error = 'Cannot login'
    data = {'api':api, 'error':error} 
    return data    


def index(request):
    tweets = []
    errors = {}
    data = get_connection()
    if data['error'] is None:
        api = data['api']
        if api is not None:
            try:
                tweets = api.GetUserTimeline()
            except NameError:
                tweets = None
                errors['NameError'] = 'Connectio Failed'   	    			 	             
    t = loader.get_template('twitter.html')
    c = RequestContext(request, {'tweets':tweets, 'errors':errors})
    return HttpResponse(t.render(c))
    

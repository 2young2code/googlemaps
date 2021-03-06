from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.conf import settings


def index(request):
    t = loader.get_template('index.html')
    user_name = getattr(settings, "USER_NAME") 
    address = request.GET.get('address', '') 
    c = RequestContext(request, {'name':user_name, 'address':address})
    return HttpResponse(t.render(c))  	
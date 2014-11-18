from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.core import serializers
import simplejson
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse



import datetime

def logeate(request):
 
	return render_to_response('logeate.html', context_instance=RequestContext(request))

def push(request):

	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse(simplejson.dumps('Login')) 
		else:
			return HttpResponse(simplejson.dumps('Desactivado')) 
	else:
		return HttpResponse(simplejson.dumps('Usuario Incorrecto'))



@login_required
def reportes(request):
 
	sms = Question.objects.all()

	#return render_to_response('reportes.html',{'sms':sms})
	
	return render_to_response('reportes.html',context_instance=RequestContext(request))

def salir(request):

	logout(request)

	return render_to_response('logeate.html', context_instance=RequestContext(request))







from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.core import serializers
import simplejson
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from MonitorApp.models import *
import datetime


def ticket(request):

	if request.method == 'POST':


		form = FormTicket(request.POST)
		id = request.user.id
		username = request.user.username
		asunto = request.POST['asunto']
		fecha_inicio = datetime.date.today()
		#estado 1=Pendiente	2=Prueba 3=Validado 4=Cerrado
		#tipo 1=Incidencia 2=Requerimento

		c=User.objects.get(pk=id).ticket_set.create(cliente=username,tipo_id=1,fecha_inicio=fecha_inicio,validado=0,estado_id=2)
		print c
		c.save()
		return render(request, 'home.html', {'form': form,'asunto':asunto})


	else:
		form = FormTicket()

	ticket_pendiente = Ticket.objects.filter(estado=1)
	ticket_cerrado = Ticket.objects.filter(estado=4)
	username = request.user.username


	return render(request, 'home.html', {'form': form,'username':username,'ticket_pendiente':ticket_pendiente,'ticket_cerrado':ticket_cerrado})

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




def salir(request):

	logout(request)

	return render_to_response('logeate.html', context_instance=RequestContext(request))







from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
import simplejson
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from MonitorApp.models import *
import datetime

def ticket_add(request):
	id = request.user.id
	ticket = Ticket.objects.filter(estado=1).order_by('-id')
	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	grupo=str(grupo)
	username = request.user.username
	tipos=Tipo.objects.all()
	estado_name=str('Nuevos')
	print estado_name

	if request.method == 'POST':


		form = FormTicket(request.POST)
		
		username = request.user.username
		asunto = request.POST['asunto']
		tipo = request.POST['tipo']
		descripcion=request.POST['descripcion']
		
		fecha_inicio = datetime.datetime.today()
		#estado 1=Nuevo	2=Atendido 3=Prueba 4=Cerrado
		#tipo 1=Incidencia 2=Requerimento


		c=User.objects.get(pk=id).ticket_set.create(cliente=username,asunto=asunto,tipo_id=1,descripcion=descripcion,fecha_inicio=fecha_inicio,validado=0,estado_id=1)
	
		c.save()
		return HttpResponseRedirect("/ticket/1")
	else:
		form = FormTicket()



	
	return render(request, 'home.html', {'estado_name':estado_name,'tipos':tipos,'form': form,'username':username,'ticket':ticket,'grupo':grupo})

def ticket(request,estado):

	id = request.user.id

	ticket = Ticket.objects.filter(estado=estado).order_by('-id')

	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	username = request.user.username
	tipos=Tipo.objects.all()
	grupo= str(grupo)
	
	if str(grupo) == 'Clientes':
		grupo_flag = 1
	else:
		grupo_flag = 0

	print grupo_flag
	if request.method == 'POST':


		form = FormTicket(request.POST)
		
		username = request.user.username
		asunto = request.POST['asunto']
		tipo = request.POST['tipo']
		descripcion=request.POST['descripcion']
		
		fecha_inicio = datetime.datetime.today()
		#estado 1=Nuevo	2=Atendido 3=Prueba 4=Cerrado
		#tipo 1=Incidencia 2=Requerimento


		c=User.objects.get(pk=id).ticket_set.create(cliente=username,asunto=asunto,tipo_id=1,descripcion=descripcion,fecha_inicio=fecha_inicio,validado=0,estado_id=1)
	
		c.save()
		
		#return render(request, 'home.html', {'username':username,'form': form,'asunto':asunto,'ticket_pendiente':ticket_pendiente,'ticket_cerrado':ticket_cerrado,'grupo':grupo,'msj':msj})

		return HttpResponseRedirect("/ticket")
	else:
		form = FormTicket()

	if str(estado)=='1': 
		estado_name= 'Nuevos'
	if str(estado)=='2': 
		estado_name= 'Atendidos'
	if str(estado)=='3': 
		estado_name= 'En Prueba'
	if str(estado)=='4': 
		estado_name= 'Cerrados'


	
	return render(request, 'home.html', {'estado_name':estado_name,'tipos':tipos,'form': form,'username':username,'ticket':ticket,'grupo':grupo,'grupo_flag':grupo_flag})

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



def editar_ticket(request,id):
	
	ticket= Ticket.objects.get(id=id)
	form = FormTicket()
	tipos=Tipo.objects.all()
	if request.method == 'POST':


		form = FormTicket(request.POST)
		username = request.user.username
		asunto = request.POST['asunto']
		tipo = request.POST['tipo']
		print tipo
		descripcion=request.POST['descripcion']
		fecha_inicio = datetime.datetime.today()

		ticket.asunto = asunto
		ticket.tipo_id =tipo
		ticket.descripcion = descripcion
		ticket.fecha_inicio =fecha_inicio
		ticket.save()
		return HttpResponseRedirect("/ticket")



	return render(request, 'editar_ticket.html', {'form': form,'ticket':ticket,'tipos':tipos})


def atender(request,id):

	ticket= Ticket.objects.get(id=id)
	ticket_pendiente = Ticket.objects.filter(estado=1).order_by('-id')
	username = request.user.username
	tipos=Tipo.objects.all()
	print username
	x=User.objects.get(username=username)
	print 'x'+str(x)
	grupo =x.groups.get()
	grupo= str(grupo)

	if ticket.estado_id ==1 :
		soporte=ticket.soporte_set.create(titulo='Soporte',fecha_inicio='2013-02-02',soporte_id=id)
		ticket.estado_id = 2
		ticket.save()
		
		msj='El ticket '+ticket.asunto+' esta siendo atendido'
		#return render(request, 'home.html', {'username':username,'grupo':grupo,'tipos':tipos,'msj':msj,'ticket':ticket_pendiente})
		return HttpResponseRedirect("/ticket/2")

	if ticket.estado_id == 2:
		msj = ''
		return HttpResponseRedirect("/ticket/2")
		#return render(request, 'home.html', {'username':username,'grupo':grupo,'tipos':tipos,'msj':msj,'ticket':ticket_pendiente})



	return HttpResponseRedirect("/ticket/2")

def cerrar(request,id):

	ticket= Ticket.objects.get(id=id)
	ticket.estado_id = 3
	ticket.save()

	return HttpResponseRedirect("/ticket/3")


def reasignar(request,id):

	ticket= Ticket.objects.get(id=id)
	username = request.user.username
	tipos=Tipo.objects.all()
	x=User.objects.get(username=username)
	soporte = User.objects.all()
	grupo =x.groups.get()
	grupo= str(grupo)
	return render(request, 'reasignar.html', {'soporte':soporte,'username':username,'grupo':grupo,'tipos':tipos,'ticket':ticket})



def ver_ticket(request,id):

	ticket= Ticket.objects.get(id=id)
	username = request.user.username
	tipos=Tipo.objects.all()
	x=User.objects.get(username=username)
	grupo =x.groups.get()
	grupo= str(grupo)


	return render(request, 'detalle.html', {'username':username,'grupo':grupo,'tipos':tipos,'ticket':ticket})


def validar(request,id):

	ticket= Ticket.objects.get(id=id)
	ticket.estado_id = 4
	ticket.save()

	return HttpResponseRedirect("/ticket/1")
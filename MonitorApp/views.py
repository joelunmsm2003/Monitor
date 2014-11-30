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
from django.core import serializers
import json  

def ver_usuario(request,id):

	usuario = User.objects.get(id=id)
	return render(request,'ver_usuario.html', {'usuario':usuario})



def agregar_ticket(request):

	id = request.user.id

	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	username = request.user.username
	tipos=Tipo.objects.all()
	grupo= str(grupo)
	
	if str(grupo) == 'Clientes':
		grupo_flag = 1
	else:
		grupo_flag = 0

	
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

		return HttpResponseRedirect("/ticket/1")
	else:
		form = FormTicket()



	return render(request,'agregar_ticket.html', {'tipos':tipos,'form': form,'username':username,'grupo':grupo,'grupo_flag':grupo_flag})


def realtime(request):

	count= Ticket.objects.count()
	ticket = Ticket.objects.all()
	id = request.user.id
	ticket = Ticket.objects.filter(estado=1).order_by('-id')
	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	grupo=str(grupo)
	username = request.user.username
	tipos=Tipo.objects.all()
	estado_name=str('Nuevos')

	return render(request, 'realtime.html', {'count':count,'estado_name':estado_name,'tipos':tipos,'username':username,'ticket':ticket,'grupo':grupo})




def realtime_post(request):

	counter = request.POST['count']
	nsoporte = request.POST['soportez']

	nsoporte_act = Soporte.objects.count()
	counter_act = Ticket.objects.count()

	
	m = {'counter_act': counter_act,'soporte_act':nsoporte_act}  
	n = json.dumps(m)  
	
	print nsoporte
	print nsoporte_act
	

	
	if ((str(counter) != str(counter_act))or(str(nsoporte)!=str(nsoporte_act))):


		print 'entro'
		ticket_nuevo = Ticket.objects.all().order_by('-id')[:1]
		soporte_nuevo = Soporte.objects.all().order_by('-id')[:1]
		soporte_nuevo = serializers.serialize("json",soporte_nuevo)
		data = serializers.serialize("json",ticket_nuevo)
		data = { 'data' : data, 'n' : n ,'snuevo':soporte_nuevo}
		data = json.dumps(data)

	
		return HttpResponse(data)
	


	return HttpResponse(n)
		


def ticket_add(request):
	id = request.user.id
	ticket = Ticket.objects.filter(estado=1).order_by('-id')
	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	grupo=str(grupo)
	username = request.user.username
	tipos=Tipo.objects.all()
	estado_name=str('Nuevos')
	

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
	count= Ticket.objects.count()
	nsoporte = Soporte.objects.count()
	
	soporte = Soporte.objects.filter(fecha_fin=None)


	x=User.objects.get(pk=id)

	grupo =x.groups.get()
	grupo= str(grupo)

	username = request.user.username
	tipos=Tipo.objects.all()
	
	if grupo == 'Clientes':
		
		ticket = Ticket.objects.filter(estado=estado,cliente_id=id).order_by('-id')
	else:
		ticket = Ticket.objects.filter(estado=estado).order_by('-id')

	
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

	return render(request, 'home.html', {'nsoporte':nsoporte,'count':count,'soporte':soporte,'estado_name':estado_name,'tipos':tipos,'form': form,'username':username,'ticket':ticket,'grupo':grupo})

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
	id_soporte = request.user.id
	tipos=Tipo.objects.all()
	
	x=User.objects.get(username=username)
	
	grupo =x.groups.get()
	grupo= str(grupo)
	fecha_inicio = datetime.datetime.today()

	if ticket.estado_id ==1 :

		soporte=ticket.soporte_set.create(fecha_inicio=fecha_inicio,soporte_id=id_soporte)
		ticket.estado_id = 2
		ticket.save()
		
		return HttpResponseRedirect("/ticket/1")




	return HttpResponseRedirect("/ticket/2")

def cerrar(request,id):

	ticket= Ticket.objects.get(id=id)
	ticket.estado_id = 3
	ticket.save()

	return HttpResponseRedirect("/ticket/3")


def reasignar(request,id,id_ticket):

	id_ticket= str(id_ticket)
	soporte= Soporte.objects.get(id=id)
	user_soporte = User.objects.filter(groups__name='Soporte')


	username = request.user.username
	tipo=Tipo.objects.all()
	x=User.objects.get(username=username)
	
	grupo =x.groups.get()
	grupo= str(grupo)

	return render(request,'reasignar.html', {'id_ticket':id_ticket ,'user_soporte':user_soporte,'soporte':soporte,'username':username,'grupo':grupo,'tipo':tipo})

def reasignar_add(request):

	if request.method == 'POST':

		form = FormTicket(request.POST)
		username = request.user.username
		soporte_user = request.POST['soporte']
		print soporte_user
		id_ticket = request.POST['id_ticket']
		ticket = Ticket.objects.get(id=id_ticket)
		id = request.POST['id']
		
		soporte = Soporte.objects.get(id=id)
		fecha_fin = datetime.datetime.today()
		soporte.fecha_fin = fecha_fin

		soporte.save()

		ticket.soporte_set.create(fecha_inicio=fecha_fin,soporte_id=soporte_user)

		return HttpResponseRedirect("/detalle_ticket/"+id_ticket+"/")


def ver_ticket(request,id):

	ticket= Ticket.objects.get(id=id)
	username = request.user.username
	
	x=User.objects.get(username=username)
	grupo =x.groups.get()
	grupo= str(grupo)


	return render(request, 'detalle.html', {'username':username,'grupo':grupo,'tipos':tipos,'ticket':ticket})


def validar(request,id):

	ticket= Ticket.objects.get(id=id)
	ticket.estado_id = 4
	fecha_fin = datetime.datetime.today()
	ticket.fecha_fin = fecha_fin
	
	ticket.save()

	return HttpResponseRedirect("/ticket/1")

def detalle_ticket(request,id):

	ticket= Ticket.objects.get(id=id)
	soportes = ticket.soporte_set.all()

	ticket.save()
	username = request.user.username
	tipos=Tipo.objects.all()
	x=User.objects.get(username=username)
	grupo =x.groups.get()
	grupo= str(grupo)

	return render(request, 'detalle_ticket.html', {'soportes':soportes,'username':username,'grupo':grupo,'tipos':tipos,'ticket':ticket})

def evento(request,id,id_ticket):

	soporte = Soporte.objects.get(id=id)
	ticket = Ticket.objects.get(id=id_ticket)
	#soporte.evento_set.create(fecha_inicio=fecha_inicio,name=name)

	return render(request, 'evento_add.html', {'ticket':ticket,'soporte':soporte})

def evento_add(request):

	
	if request.method == 'POST':

		evento_id = request.POST['id_ticket']
		soporte_id = request.POST['id']
		user = 	request.user.id	
		name = request.POST['name']
		fecha_inicio = datetime.datetime.today()

		soporte = Soporte.objects.get(id=soporte_id)
		soporte.evento_set.create(fecha_inicio=fecha_inicio,name=name,user_id=user)

		return HttpResponseRedirect("/ver_evento/"+soporte_id+"/"+evento_id)

def ver_evento(request,id,id_ticket):

	ticket = Ticket.objects.get(id=id_ticket)
	soporte = Soporte.objects.get(id=id)
	evento = soporte.evento_set.all()
	
	#soporte.evento_set.create(fecha_inicio=fecha_inicio,name=name)

	return render(request, 'ver_evento.html', {'evento':evento,'soporte':soporte,'ticket':ticket})



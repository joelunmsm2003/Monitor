from django.db import models
from django.contrib.auth.models import User
from django import forms

class FormTicket(forms.Form):

    cc_myself = forms.BooleanField(required=False)


class Tipo(models.Model):

	name = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateField(null=True,blank=True)
	comentario = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Estado(models.Model):

	name = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateField(null=True,blank=True)
	comentario = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Ticket(models.Model):

	cliente = models.ForeignKey(User)
	titulo = models.CharField(max_length=100,blank=True)
	tipo = models.ForeignKey(Tipo)
	problema = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField(null=True,blank=True)
	validado = models.BooleanField(max_length=100,blank=True)
	estado = models.ForeignKey(Estado)
	comentario = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.titulo

class Soporte(models.Model):

	ticket = models.ForeignKey(Ticket)
	titulo = models.CharField(max_length=100,primary_key=True)

	fecha_inicio = models.DateField()
	fecha_fin= models.DateField(null=True,blank=True)
	soporte = models.ForeignKey(User,)
	comentario = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.titulo

class Evento(models.Model):

	evento = models.ForeignKey(Ticket)
	name = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateField(null=True,blank=True)
	comentario = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.name















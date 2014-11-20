from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
	
	name = models.CharField(max_length=100)
	comentario = models.CharField(max_length=100)
	fecha_inicio = models.DateField()

class Cliente(models.Model):

	user = models.ForeignKey(User,)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	celular = models.CharField(max_length=100)
	empresa = models.ForeignKey(Empresa)
	comentario = models.CharField(max_length=100)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()

class Soporte(models.Model):

	user = models.ForeignKey(User,)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	celular = models.CharField(max_length=100)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	comentario = models.CharField(max_length=100)

class Estado(models.Model):

	name = models.CharField(max_length=100)
	fecha_inicio = models.DateField()
	comentario = models.CharField(max_length=100)


class Tarea(models.Model):

	estado = models.ForeignKey(Estado)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	comentario = models.CharField(max_length=100)

class Cliente_soporte(models.Model):
	
	cliente = models.ForeignKey(Cliente)
	soporte = models.ForeignKey(Soporte)
	tarea = models.CharField(Tarea,max_length=100)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	comentario = models.CharField(max_length=100)


class Eventos(models.Model):

	cliente_soporte = models.ForeignKey(Cliente_soporte)
	comentario = models.CharField(max_length=100)
	fecha_inicio = models.DateField()









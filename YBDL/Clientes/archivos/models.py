from django.db import models
class Facturas(models.Model):
    fecha_de_emision=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    link=models.CharField(max_length=2000)
class Recibos(models.Model):
    fecha_de_emision=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    link=models.CharField(max_length=2000)
class Retenciones(models.Model):
    fecha_de_emision=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    link=models.CharField(max_length=2000)
class reclamo(models.Model):
    fecha_de_emision=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    link=models.CharField(max_length=2000)
# Create your models here.

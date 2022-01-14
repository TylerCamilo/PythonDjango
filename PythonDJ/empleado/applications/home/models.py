#from os import name
from django.db import models

# Create your models here.

#creacion una base de datos 
#una clase que tenga herencia

class Prueba(models.Model):
    titulo = models.CharField(max_length = 100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

def __string__(Self):
    return Self.titulo + Self.subtitulo
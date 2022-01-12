from django.db import models
from django.db.models.fields import CharField
from applications.departamento.models import Departamento

# Create your models here.
 
class Empleado(models.Model):
     """Modelo para tabla empleado"""
     jobChoices= (('0','Contador'),('1','Administrador'),
                    ('2', 'Economista'),('3','Otro'))
     #contador,administrador, economista, otro
     first_name = models.CharField("Nombres", max_length=60)
     last_name = models.CharField("Apellidos", max_length=60)
     job = models.CharField("Trabajo", max_length=60, choices=jobChoices)
     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
     #image = models.ImageField (upload_to=None, height_field= None,width_field=None, max_lenth=None)

     def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
    
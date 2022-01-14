from django.db import models
from django.db.models.fields import CharField
from applications.departamento.models import Departamento

# Create your models here.
class Habilidades(models.Model):
      habilidad = models.CharField('Habilidad', max_length = 50)

      class Meta:
         verbose_name = 'Habilidad'
         verbose_name_plural = 'Habilidades empleados'

      def __str__(self):
        return str(self.id) + ' - ' + self.habilidad
    

 
class Empleado(models.Model):
     """Modelo para tabla empleado"""
     jobChoices= (('0','Contador'),
                  ('1','Administrador'),
                  ('2', 'Economista'),
                  ('3','Otro'))

     #contador,administrador, economista, otro
     first_name = models.CharField("Nombres", max_length=60)
     last_name = models.CharField("Apellidos", max_length=60)
     job = models.CharField("Trabajo", max_length=60, choices=jobChoices)
     departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
     avatar = models.ImageField (upload_to = 'empleado', blank = True, null = True)
     habilidades = models.ManyToManyField(Habilidades) 
     
     class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name', 'last_name']
        unique_together = ('first_name','departamento')
     
     def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
    
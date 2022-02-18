from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    short_name = models.CharField('Nombre Corto', max_length = 20,unique=True)
    anulate = models.BooleanField('Anulado', default = False)
    
    class Meta: #Decorador u ordenador
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering =['name'] #ordenar
        unique_together = ('name', 'short_name') #no permite registro repetido
        
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name 
     
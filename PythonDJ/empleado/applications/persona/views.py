from pyexpat import model
from django.shortcuts import render
from django.views.generic import (ListView)

#models
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 5
    ordering = 'first_name'
    model = Empleado
    
    
class ListByAreaEmpleados(ListView): #lista empleados de un area
    template_name = 'persona/list_by_area.html'
    
    def get_queryset(self):
        
        area =  self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__name = area
        )
        return lista
    
class ListEmpleadosByKword(ListView):
    #Lista de empleado por palabra clave
    template_name = 'persona/by_kword.html' #Cxreamos el template a usar 
    context_object_name = 'empleados' #redefinir el nombre con el que se accede al resultado
        
    def get_queryset(self):
        print('Aqui es ****')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        ) 
        print('lista restultado: ', lista)
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    
    
    #context_object_name = 'lista'
# Create your views here.
# Listar lso empleados de la empresa
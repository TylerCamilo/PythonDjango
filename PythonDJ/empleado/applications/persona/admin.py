from re import search
from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


admin.site.register(Habilidades)

#Decorador para que muestre los datos en columnas
class EmpleadoAdmin(admin.ModelAdmin): #heredando funciones
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
         
    )
    #funcion de full_name
    
    def full_name(self,obj):
        #la funcion que se neceite
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name
    
    search_fields = ('first_name' ,)
    list_filter = ('job',"departamento", 'habilidades',)
    #
    filter_horizontal = ('habilidades',)
    
    
admin.site.register(Empleado, EmpleadoAdmin)
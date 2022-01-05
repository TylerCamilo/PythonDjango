from django.contrib import admin
from django.urls import path

def DesdeApp(self):
    print('===================estamos probando URLS.py desde la app deparatamento')

urlpatterns = [
    path('departamento/', DesdeApp),
]

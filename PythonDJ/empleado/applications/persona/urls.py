from django.contrib import admin
from django.urls import path

def DesdeApp1(self):
    print('===================estamos probando URLS.py desde la app persona')

urlpatterns = [
    path('persona/', DesdeApp1),
]

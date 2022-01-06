from django.contrib import admin
from django.urls import path

def DesdeApp(self):
    print('====DESDE_DEPARTAMENTO====')

urlpatterns = [
    path('departamento/', DesdeApp),
]

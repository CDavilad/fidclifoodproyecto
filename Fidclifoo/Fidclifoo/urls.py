"""Fidclifoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from compras import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('tienda/<str:nombretienda>/', views.tienda, name='tienda'),
    path('registro/', views.registro, name="registro"),
    path('perfil/', views.perfil, name='perfil'),
    path('iniciar_sesion/', views.index, name='index'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('guardar_carro/', views.guardar_carro, name="guardar"),
    path('historial/', views.historial, name = 'historial'),
]

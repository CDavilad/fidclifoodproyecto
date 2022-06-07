from django.contrib import admin
from .models import Perfil, Producto, Tienda, Comentario
# Register your models here.

admin.site.register(Perfil)
admin.site.register(Tienda)
admin.site.register(Producto)
admin.site.register(Comentario)
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save 
# Create your models here.
from django.contrib.auth.models import User
from PIL import Image

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.IntegerField(null=True)
    puntos = models.IntegerField(default=0)
    @receiver(post_save, sender = User)
    def crear_perfil_usuario(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def guardar_perfil_usuario(sender, instance, **kwargs):
        instance.perfil.save()
    
    def __str__(self) -> str:
        return f'{self.user.username} Perfil'

class Tienda(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to = 'compras/tiendas/')

    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=240)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to = 'compras/productos/')
    disponibilidad = models.BooleanField(default=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    valoracion = models.IntegerField(default=0)
    
    class Categoria(models.TextChoices):
        Hamburguesa = "Hamburguesa"
        Perro = "Perro"
        Pollo = "Pollo"
        Papas = "Papa"
        Postre = "Postre"
        Combo = "Combo"
        Acompanante = "Acompanante" 

    categoria = models.CharField(max_length=11, choices = Categoria.choices, default=Categoria.Hamburguesa)

    def __str__(self):
        return f'{self.tienda}---{self.nombre}-{self.precio}-{self.categoria}'

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    contenido = models.CharField(max_length=500)
    fecha = models.DateTimeField()


class Orden(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    entregado = models.BooleanField(default=False)
    productos = models.ManyToManyField(Producto)
    fechapedido = models.DateTimeField(auto_now=True)
    total = models.IntegerField()
    


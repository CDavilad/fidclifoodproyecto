from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import CrearUsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CrearUsuarioForm, UserForm, PerfilForm
from .models import Perfil, Producto, Tienda, Orden
from PIL import Image
from .Carrito import Carrito
# Create your views here.

def index(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has ingresado como {username}")
                return redirect("inicio")
            else:
                messages.error(request, "Usuario o contraseña inválidos")
        messages.error(request, "Usuario o contraseña inválidos")
    form = AuthenticationForm()
    return render(request=request, template_name="index.html", context={"login_form":form})

def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Has cerrado sesion con éxito")
    return redirect("index")


def registro(request):
    mensaje = "a"
    if request.method == "POST":
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect("inicio")
        mensaje = messages.error(request, "Registro no exitoso. Información inválida")
    form = CrearUsuarioForm()
    return render(request=request, template_name="registro.html", context={"register_form":form, "mensaje":mensaje})

def inicio(request):
    if  not request.user.is_authenticated:
        return redirect("index")

    tiendas = Tienda.objects.all()
    user = request.user
    return render(request,'inicio.html', {'tiendas' : tiendas, 'user':user})

def tienda(request, nombretienda):
    if  not request.user.is_authenticated:
        return redirect("index")
    tienda = Tienda.objects.get(nombre = nombretienda)
    productos = Producto.objects.filter(tienda = tienda)
    return render(request, 'tienda.html', {'productos':productos,'tienda':tienda})

def perfil(request):
    if  not request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = PerfilForm(request.POST, instance=request.user.perfil)
        if user_form.is_valid():
            user_form.save()
        elif profile_form.is_valid():
            profile_form.save()
        else:
            messages.error(request, ('Imposible continuar'))
        return redirect("perfil")
    user_form = UserForm(instance=request.user)
    profile_form = PerfilForm(instance=request.user.perfil)
    return render(request=request, template_name="perfil.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    tienda = producto.tienda.nombre
    tienda1 = Tienda.objects.get(nombre = tienda)
    productos = Producto.objects.filter(tienda = tienda1)
    return redirect("tienda", tienda)

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    tienda = producto.tienda.nombre
    tienda1 = Tienda.objects.get(nombre = tienda)
    return redirect("tienda", tienda)

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    tienda = producto.tienda.nombre
    tienda1 = Tienda.objects.get(nombre = tienda)
    carrito.restar(producto)
    return redirect("tienda", tienda)

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("inicio")

def guardar_carro(request):
    carrito = Carrito(request)
    compra = Orden(user = request.user, total = carrito.total)
    compra.save()
    
    producto = Producto.objects.get(nombre = "McBacon")
    total = producto.precio
    compra.productos.add(producto)
    compra.total = total
    compra.save()
    carrito.limpiar()
    return redirect("inicio")

def historial(request):
    ordenes = Orden.objects.filter(user = request.user)
    return render(request=request, template_name="historial.html", context={"user":request.user, "ordenes":ordenes})
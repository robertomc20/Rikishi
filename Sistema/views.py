from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Perfil
from .models import Producto
from .models import Detalle_Pedido
from .forms import SignUpForm,AgregarProducto,AgregarDetalle
"""from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm"""
from django.db.models import DEFERRED
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def inicio(request):
    return render (request,"inicio.html")

    
def base_layout(request):
    return render(request,"maqueta.html")


def registroCliente(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST or None)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = SignUpForm()
    return render (request,"registroCliente.html", {'form':form})


def loginCliente(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request,'loginCliente.html', {'form':form})


def logoutCliente(request):
    logout(request)
    return redirect('inicio')


def gestionProducto(request):
    form=AgregarProducto(request.POST or None,request.FILES or None)
    if form.is_valid():
        datos=form.cleaned_data
        regDb=Producto(nombreProducto=datos.get("nombreProducto"),precioProducto=datos.get("precioProducto"),descripcion=datos.get("descripcion"),
        stockProducto=datos.get("stockProducto"),fotoProducto=datos.get("fotoProducto"))
        regDb.save()
    producto=Producto.objects.all()
    contexto={
        'producto':producto,
        'form':form,
    }
    return render (request,"gestionProducto.html",contexto)


def editarProducto(request, pk):
    producto=Producto.objects.get(codigoProducto=pk)
    if request.method == "GET":
        form = AgregarProducto(instance=producto)
    else:
        form = AgregarProducto(request.POST or None,request.FILES or None,instance=producto)
        if form.is_valid():
            form.save()
        return redirect('gestionProducto')
    return render(request, 'editarProducto.html', {'form':form})
    

def eliminarProducto(request, pk):
    producto=Producto.objects.get(codigoProducto=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('gestionProducto')
    return render (request, 'eliminarProducto.html', {'producto':producto})


def verProductos(request):
    producto=Producto.objects.all()
    pedido=Detalle_Pedido.objects.filter(cliente=request.user.username)
    contexto={
        'pedido':pedido,
        'producto':producto,
    }
    return render (request,"verProductos.html",contexto)





def añadirProducto(request,pk):
    producto=Producto.objects.get(codigoProducto=pk)
    pedido=Detalle_Pedido.objects.all()
    if request.method == "GET":
        form = AgregarDetalle(instance=producto)
    else:
        form = AgregarDetalle(request.POST or None,request.FILES or None,instance=producto)
        if form.is_valid():
            datos=form.cleaned_data
            regDb=Detalle_Pedido(codigoProducto=datos.get("codigoProducto"),nombreProducto=datos.get("nombreProducto"),precioProducto=datos.get("precioProducto"),cliente=request.user.username)
            regDb.save()
            form.save()
        return redirect('verProductos')
    return render(request, 'añadirProducto.html', {'form':form,'producto':producto})


def eliminarPedido(request, pk):
    pedido=Detalle_Pedido.objects.get(codigoPedido=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect('verProductos')
    return render (request, 'eliminarPedido.html', {'pedido':pedido})

def mostrarPedido(request):
    Detalle_Pedido.objects.all().delete
    
    return render (request,"pedido.html")
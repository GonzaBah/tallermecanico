from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
# Create your views here.

def inicio(request):
    return render(request, 'productos.html')

def stock(request, id, num):
    producto = Producto.objects.get(id = id)
    producto.stockProducto = producto.stockProducto + num
    
    producto.save()

    messages.success(request, 'Perfil modificado correctamente!')
    return redirect('productos')

def productos(request):
    producto = Producto.objects.all()
    contexto = {"pro": producto}
    return render(request, 'productos.html', contexto)
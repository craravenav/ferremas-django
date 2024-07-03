from django.shortcuts import render

# Create your views here.
def index(request):
    return render ( request , 'tienda/index.html')

def tienda(request):
    context = {}
    return render (request, 'tienda/tienda.html',context)

def contactanos(request):
    return render ( request , 'tienda/contactanos.html')

def pedidos(request):
    context = {}
    return render (request, 'tienda/pedidos.html',context)

def pagos(request):
    context = {}
    return render (request, 'tienda/pagos.html',context)
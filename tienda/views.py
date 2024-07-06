from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import ContactoForm, ProductoForm

# Create your views here.
def index(request):
    categorias = Categoria.objects.all()
    context = { 
        'categorias': categorias
    }
    return render ( request , 'tienda/index.html', context)

def tienda(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    context = { 
        'productos': productos,
        'categorias': categorias
    }
    return render (request, 'tienda/tienda.html',context)

def contactanos(request):
    categorias = Categoria.objects.all()
    context = { 
        'categorias': categorias,
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje"] = "Mensaje Enviado con exito!"
        else:
            context["form"] = formulario

    return render ( request , 'tienda/contactanos.html', context)

def pedidos(request):
    context = {}
    return render (request, 'tienda/pedidos.html',context)

def pagos(request):
    context = {}
    return render (request, 'tienda/pagos.html',context)

# CRUD DE PRODUCTO
def agregar_producto(request):
    
    context = { 
        'form': ProductoForm()
    }

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST,request.FILES)
        
        if producto_form.is_valid():
            producto = producto_form.save() 
            context["mensaje"] = "Producto Agregado con exito!"
        else:
            context["form"] = producto_form

    return render (request, 'tienda/producto/agregar.html', context)

def listar_producto(request):
    productos = Producto.objects.all()
    context = { 
        'productos': productos
    }
    return render (request, 'tienda/producto/listar.html', context)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    
    context = {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES, instance=producto)
        
        if producto_form.is_valid():
            producto = producto_form.save()  
            return redirect(to="listar_producto")
        else:
            context["form"] = producto_form


    return render(request, 'tienda/producto/modificar.html', context)

def eliminar_producto(request, id):
    producto = get_object_or_404(id=id)
    producto.delete()
    return redirect(to="listar_producto")


# CRUD DE MARCA
def agregar_marca(request):
    context = { 
        
    }
    return render (request, 'tienda/marca/agregar.html', context)

def listar_marca(request):
    context = { 
    }
    return render (request, 'tienda/marca/listar.html', context)

# CRUD DE CATEGORIA
def agregar_categoria(request):
    context = { 
        
    }
    return render (request, 'tienda/categoria/agregar.html', context)

def listar_categoria(request):
    context = { 
    }
    return render (request, 'tienda/categoria/listar.html', context)



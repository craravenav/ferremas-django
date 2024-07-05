from django.shortcuts import render
from .models import Producto, Categoria, ImagenProducto
from .forms import ContactoForm, ProductoForm, ImagenProductoForm

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
        'producto_form': ProductoForm(),
        'imagenes_form': ImagenProductoForm()
    }

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        imagen_form = ImagenProductoForm(request.POST, request.FILES)
        
        if producto_form.is_valid() and imagen_form.is_valid():
            producto = producto_form.save()  # Guardar el producto primero
            imagen = imagen_form.save(commit=False)
            imagen.producto = producto  # Asignar el producto a la imagen
            imagen.save()  
            
            context["mensaje"] = "Producto Agregado con exito!"
        else:
            context["producto_form"] = producto_form
            context["imagenes_form"] = imagen_form

    return render (request, 'tienda/producto/agregar.html', context)

def listar_producto(request):
    context = { 
    }
    return render (request, 'tienda/producto/listar.html', context)

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



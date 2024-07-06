from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Marca
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, MarcaForm, CategoriaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

#SESIONES LOGIN, LOGOUT, REGISTRO
def logout_view(request):
    logout(request)
    messages.success(request, "Gracias por visitarnos sesión cerrada!")
    return redirect('index') 

def registro(request):
    context={'form': CustomUserCreationForm()}

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect(to="index")
        context["form"] = formulario

    return render(request, 'registration/registro.html',context)

# PAGINA DE INICIO
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
@permission_required('tienda.add_producto')
def agregar_producto(request):
    
    context = { 
        'form': ProductoForm()
    }

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST,request.FILES)
        
        if producto_form.is_valid():
            producto = producto_form.save() 
            messages.success(request, "Producto Agregado Correctamente")
            return redirect(to='listar_producto')
        else:
            context["form"] = producto_form

    return render (request, 'tienda/producto/agregar.html', context)

@permission_required('tienda.view_producto')
def listar_producto(request):
    productos = Producto.objects.all()
    context = { 
        'productos': productos
    }
    return render (request, 'tienda/producto/listar.html', context)

@permission_required('tienda.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    
    context = {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES, instance=producto)
        
        if producto_form.is_valid():
            producto = producto_form.save()  
            messages.success(request, "Producto Modificado Correctamente")
            return redirect(to="listar_producto")
        else:
            context["form"] = producto_form


    return render(request, 'tienda/producto/modificar.html', context)

@permission_required('tienda.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")
    return redirect(to="listar_producto")


# CRUD DE MARCA
@permission_required('tienda.add_marca')
def agregar_marca(request):
    context = { 
        'form': MarcaForm()
    }

    if request.method == 'POST':
        form = MarcaForm(request.POST)
        
        if form.is_valid():
            marca = form.save() 
            messages.success(request, "Marca Agregada Correctamente")
            return redirect(to='listar_marca')
        else:
            context["form"] = form

    return render (request, 'tienda/marca/agregar.html', context)

@permission_required('tienda.view_marca')
def listar_marca(request):
    marcas = Marca.objects.all()
    context = { 
        'marcas': marcas
    }
    return render (request, 'tienda/marca/listar.html', context)

@permission_required('tienda.change_marca')
def modificar_marca(request, id):

    marca = get_object_or_404(Marca, id=id)
    
    context = {
        'form':MarcaForm(instance=marca)
    }

    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        
        if form.is_valid():
            marca = form.save()  
            messages.success(request, "Marca Modificada Correctamente")
            return redirect(to="listar_marca")
        else:
            context["form"] = form


    return render(request, 'tienda/marca/modificar.html', context)

@permission_required('tienda.delete_marca')
def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    messages.success(request, "Marca Eliminada Correctamente")
    return redirect(to="listar_marca")


# CRUD DE CATEGORIA
@permission_required('tienda.add_categoria')
def agregar_categoria(request):
    context = { 
        'form': CategoriaForm()
    }

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        
        if form.is_valid():
            categoria = form.save() 
            messages.success(request, "Categoria Agregada Correctamente")
            return redirect(to='listar_categoria')
        else:
            context["form"] = form

    return render (request, 'tienda/categoria/agregar.html', context)

@permission_required('tienda.view_categoria')
def listar_categoria(request):
    categorias = Categoria.objects.all()
    context = { 
        'categorias': categorias
    }
    return render (request, 'tienda/categoria/listar.html', context)

@permission_required('tienda.change_categoria')
def modificar_categoria(request, id):

    categoria = get_object_or_404(Categoria, id=id)
    
    context = {
        'form':CategoriaForm(instance=categoria)
    }

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        
        if form.is_valid():
            marca = form.save()  
            messages.success(request, "Categoria Modificada Correctamente")
            return redirect(to="listar_categoria")
        else:
            context["form"] = form


    return render(request, 'tienda/categoria/modificar.html', context)

@permission_required('tienda.delete_categoria')
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, "Categoria Eliminada Correctamente")
    return redirect(to="listar_categoria")
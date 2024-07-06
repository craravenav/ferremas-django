from django.db import models
from django.contrib.auth.models import User


# CATEGORIA PRODUCTO
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# MARCA PRODUCTO
class Marca(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
# PRODUCTO
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)

    def __str__(self):
        return self.nombre
    
# CLIENTE
EMPLEADO_ROLES = [
    ('Contador', 'contador'),
    ('Bodeguero', 'bodeguero')
]

# USER EMPLEADO
class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empleado_rol = models.CharField(max_length=10, choices=EMPLEADO_ROLES)
    rut = models.CharField(max_length=10, null=False, primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

# USER CLIENTE 
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.TextField()
    rut = models.CharField(max_length=10, null=False, primary_key=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

# PEDIDO
opciones_estadoPedido = [
    [0,"En Preparación"],
    [1,"Enviado"],
    [2,"Recepcionado"],
    [3,"Pagado"]
]

class Pedido(models.Model):
    fecha = models.DateField()
    total = models.IntegerField()
    estado = models.IntegerField(choices=opciones_estadoPedido)
    vendedor = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

# DETALLE PEDIDO
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    subtotal = models.IntegerField()

# CONTACTO
opciones_consulta = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre 
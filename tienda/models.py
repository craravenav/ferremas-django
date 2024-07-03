from django.db import models

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
    

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to="productos", null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="imagenes")

# CLIENTE


# PEDIDO
opciones_estadoPedido = [
    [0,"En Preparación"],
    [1,"Enviado"],
    [2,"Recepcionado"]
]

class Pedido(models.Model):
    fecha = models.DateField()
    total = models.IntegerField()
    estado = models.IntegerField(choices=opciones_estadoPedido)
    
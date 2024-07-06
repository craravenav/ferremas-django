from django.contrib import admin
from .models import Marca, Categoria, Producto, Contacto, Pedido, Cliente, Empleado



class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca", "categoria"]
    list_editable = ["precio","categoria"]

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Pedido)




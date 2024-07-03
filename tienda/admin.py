from django.contrib import admin
from .models import Marca, Categoria, ImagenProducto, Producto

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca", "categoria"]
    list_editable = ["precio","categoria"]
    inlines = [
        ImagenProductoAdmin
    ]

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)


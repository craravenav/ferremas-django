from django.urls import path
from .views import index, tienda, pedidos,contactanos,pagos,agregar_producto, listar_producto,agregar_marca,listar_marca,agregar_categoria,listar_categoria, modificar_producto, eliminar_producto

urlpatterns = [
    path('',index ,name='index'),
    path('tienda',tienda,name='tienda'),
    path('pedidos',pedidos,name='pedidos'),
    path('contactanos',contactanos,name='contactanos'),
    path('pagos',pagos,name='pagos'),
    path('agregar-producto',agregar_producto,name='agregar_producto'),
    path('listar-producto',listar_producto,name='listar_producto'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('agregar-categoria',agregar_categoria,name='agregar_categoria'),
    path('listar-categoria',listar_categoria,name='listar_categoria'),
    path('agregar-categoria',agregar_marca,name='agregar_marca'),
    path('listar-categoria',listar_marca,name='listar_marca'),

]
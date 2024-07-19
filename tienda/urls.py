from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index , name='index'),
    path('tienda', views.tienda, name='tienda'),
    path('pedidos', views.pedidos, name='pedidos'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('pagos', views.pagos, name='pagos'),
    path('agregar-producto', views.agregar_producto, name='agregar_producto'),
    path('listar-producto', views.listar_producto, name='listar_producto'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/',  views.eliminar_producto, name='eliminar_producto'),
    path('agregar-categoria', views.agregar_categoria, name='agregar_categoria'),
    path('listar-categoria', views.listar_categoria, name='listar_categoria'),
    path('modificar-categoria/<id>/', views.modificar_categoria, name='modificar_categoria'),
    path('eliminar-categoria/<id>/',  views.eliminar_categoria, name='eliminar_categoria'),
    path('agregar-marca', views.agregar_marca, name='agregar_marca'),
    path('listar-marca', views.listar_marca, name='listar_marca'),
    path('modificar-marca/<id>/', views.modificar_marca, name='modificar_marca'),
    path('eliminar-marca/<id>/',  views.eliminar_marca, name='eliminar_marca'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('registro', views.registro, name ='registro'),

    path('agregar-pedido', views.agregar_pedido, name='agregar_pedido'),
    path('listar-pedido', views.listar_pedido, name='listar_pedido'),
    path('eliminar_pedido/<pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
]
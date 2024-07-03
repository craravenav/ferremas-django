from django.urls import path
from .views import index, tienda, pedidos,contactanos,pagos

urlpatterns = [
    path('',index ,name='index'),
    path('tienda',tienda,name='tienda'),
    path('pedidos',pedidos,name='pedidos'),
    path('contactanos',contactanos,name='contactanos'),
    path('pagos',pagos,name='pagos')
]
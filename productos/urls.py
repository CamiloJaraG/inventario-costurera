from django.urls import path
from productos.views import *

urlpatterns = [
    path('crearcliente/', crearCliente, name='crear_cliente'),
    path('listarclientes/', listarClientes, name='listar_clientes'),
    path('editarcliente/<int:id>/', editarCliente, name='editar_cliente'),
    path('eliminarcliente/<int:id>/', eliminarCliente, name='eliminar_cliente'),
    path('crearvestimenta/', crearVestimenta, name='crear_vestimenta'),
    path('listarvestimentas/', listarVestimentas, name='listar_vestimentas'),
    path('editarvestimenta/<int:id>/', editarVestimenta, name='editar_vestimenta'),
    path('eliminarvestimenta/<int:id>/', eliminarVestimenta, name='eliminar_vestimenta'),
]
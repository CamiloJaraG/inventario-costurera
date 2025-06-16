from django.urls import path
from productos.views import *

urlpatterns = [
    # Inicio y cierre de sesión
    path('login/', inicioSesion, name='login'),
    path('logout/', cerrarSesion, name='logout'),

    # Cliente
    path('crearcliente/', crearCliente, name='crear_cliente'),
    path('listarclientes/', listarClientes, name='listar_clientes'),
    path('editarcliente/<int:id>/', editarCliente, name='editar_cliente'),
    path('eliminarcliente/<int:id>/', eliminarCliente, name='eliminar_cliente'),

    # Vestimenta
    path('crearvestimenta/', crearVestimenta, name='crear_vestimenta'),
    path('listarvestimentas/', listarVestimentas, name='listar_vestimentas'),
    path('editarvestimenta/<int:id>/', editarVestimenta, name='editar_vestimenta'),
    path('eliminarvestimenta/<int:id>/', eliminarVestimenta, name='eliminar_vestimenta'),

    # Tipo de pago
    path('creartipopago/', crearTipoPago, name='crear_tipo_pago'),
    path('listartipopagos/', listarTipoPagos, name='listar_tipo_pagos'),
    path('editartipopago/<int:id>/', editarTipoPago, name='editar_tipo_pago'),
    path('eliminartipopago/<int:id>/', eliminarTipoPago, name='eliminar_tipo_pago'),

    # Tipo de material
    path('creartipomaterial/', crearTipoMaterial, name='crear_tipo_material'),
    path('listartipomateriales/', listarTipoMateriales, name='listar_tipo_materiales'),
    path('editartipomaterial/<int:id>/', editarTipoMaterial, name='editar_tipo_material'),
    path('eliminartipomaterial/<int:id>/', eliminarTipoMaterial, name='eliminar_tipo_material'),

    # Tipo de cliente
    path('creartipocliente/', crearTipoCliente, name='crear_tipo_cliente'),
    path('listartipoclientes/', listarTipoClientes, name='listar_tipo_clientes'),
    path('editartipocliente/<int:id>/', editarTipoCliente, name='editar_tipo_cliente'),
    path('eliminartipocliente/<int:id>/', eliminarTipoCliente, name='eliminar_tipo_cliente'),

    # Material
    path('crearmaterial/', crearMaterial, name='crear_material'),
    path('listarmateriales/', listarMateriales, name='listar_materiales'),
    path('editarmaterial/<int:id>/', editarMaterial, name='editar_material'),
    path('eliminarmaterial/<int:id>/', eliminarMaterial, name='eliminar_material'),

    # Tipo de vestimenta
    path('creartipovestimenta/', crearTipoVestimenta, name='crear_tipo_vestimenta'),
    path('listartipovestimentas/', listarTipoVestimentas, name='listar_tipo_vestimentas'),
    path('editartipovestimenta/<int:id>/', editarTipoVestimenta, name='editar_tipo_vestimenta'),
    path('eliminartipovestimenta/<int:id>/', eliminarTipoVestimenta, name='eliminar_tipo_vestimenta'),

    # Tipo de pedido
    path('creartipopedido/', crearTipoPedido, name='crear_tipo_pedido'),
    path('listartipopedidos/', listarTipoPedidos, name='listar_tipo_pedidos'),
    path('editartipopedido/<int:id>/', editarTipoPedido, name='editar_tipo_pedido'),
    path('eliminartipopedido/<int:id>/', eliminarTipoPedido, name='eliminar_tipo_pedido'),
    
    # Producto
    path('crearproducto/', crearProducto, name='crear_producto'),
    path('listarproductos/', listarProductos, name='listar_productos'),
    path('editarproducto/<int:id>/', editarProducto, name='editar_producto'),
    path('eliminarproducto/<int:id>/', eliminarProducto, name='eliminar_producto'),

    # Pedido
    path('crearpedido/', crearPedido, name='crear_pedido'),
    path('listarpedidos/', listarPedidos, name='listar_pedidos'),
    path('editarpedido/<int:id>/', editarPedido, name='editar_pedido'),
    path('eliminarpedido/<int:id>/', eliminarPedido, name='eliminar_pedido'),

    # Venta
    path('crearventa/', crearVenta, name='crear_venta'),
    path('listarventas/', listarVentas, name='listar_ventas'),
    path('editarventa/<int:id>/', editarVenta, name='editar_venta'),
    path('eliminarventa/<int:id>/', eliminarVenta, name='eliminar_venta'),
]
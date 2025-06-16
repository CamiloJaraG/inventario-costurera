# archivo: productos/management/commands/poblar_datos.py

from django.core.management.base import BaseCommand
from productos.models import *
from django.utils import timezone
from random import randint, choice

class Command(BaseCommand):
    help = 'Poblar la base de datos con datos de prueba'

    def handle(self, *args, **kwargs):
        # Tipos básicos
        tipos_cliente = ['Mayorista', 'Minorista', 'Frecuente']
        tipos_material = ['Algodón', 'Lana', 'Seda']
        tipos_pago = ['Efectivo', 'Transferencia', 'Débito']
        tipos_vestimenta = ['Camisa', 'Pantalón', 'Falda']
        tipos_pedido = ['Normal', 'Urgente']

        for tipo in tipos_cliente:
            TipoCliente.objects.get_or_create(tipo=tipo)
        for tipo in tipos_material:
            TipoMaterial.objects.get_or_create(nombre=tipo)
        for tipo in tipos_pago:
            TipoPago.objects.get_or_create(tipo=tipo)
        for tipo in tipos_vestimenta:
            TipoVestimenta.objects.get_or_create(tipo=tipo)
        for tipo in tipos_pedido:
            TipoPedido.objects.get_or_create(tipo=tipo)

        # Materiales
        for i in range(1, 6):
            Material.objects.get_or_create(
                nombre=f"Material {i}",
                descripcion="Material de prueba",
                cantidad=randint(0, 50),
                precio_unitario=randint(1000, 5000),
                fecha_entrada=timezone.now().date(),
                tipo_material=TipoMaterial.objects.order_by('?').first()
            )

        # Clientes
        for i in range(1, 6):
            Cliente.objects.get_or_create(
                nombre=f"Cliente{i}",
                apellido=f"Apellido{i}",
                correo=f"cliente{i}@correo.com",
                telefono=f"+5691234567{i}",
                tipo_cliente=TipoCliente.objects.order_by('?').first()
            )

        # Vestimentas
        for i in range(1, 6):
            Vestimenta.objects.get_or_create(
                nombre=f"Vestimenta {i}",
                precio=randint(5000, 15000),
                tipo_vestimenta=TipoVestimenta.objects.order_by('?').first()
            )

        # Productos
        for i in range(1, 6):
            Producto.objects.get_or_create(
                nombre=f"Producto {i}",
                cantidad=randint(0, 30),
                fecha_produccion=timezone.now().date(),
                material=Material.objects.order_by('?').first(),
                vestimenta=Cliente.objects.order_by('?').first()
            )

        # Pedidos
        for i in range(1, 6):
            Pedido.objects.get_or_create(
                nombre=f"Pedido {i}",
                cantidad=randint(1, 20),
                fecha_pedido=timezone.now().date(),
                producto=Producto.objects.order_by('?').first(),
                cliente=Cliente.objects.order_by('?').first(),
                tipo_pedido=TipoPedido.objects.order_by('?').first()
            )

        # Ventas
        for i in range(1, 6):
            Venta.objects.get_or_create(
                descripcion=f"Venta generada {i}",
                precio=randint(10000, 40000),
                fecha_venta=timezone.now().date(),
                pedido=Pedido.objects.order_by('?').first(),
                tipo_pago=TipoPago.objects.order_by('?').first()
            )

        self.stdout.write(self.style.SUCCESS('Datos de prueba insertados exitosamente.'))

from django.db import models

""" Entidades fuertes """
class TipoCliente(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'tipos_clientes'
        verbose_name = "Tipo de Cliente"
        verbose_name_plural = "Tipos de Clientes"

class TipoMaterial(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tipos_materiales'
        verbose_name = "Tipo de Material"
        verbose_name_plural = "Tipos de Materiales"

class TipoPago(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'tipos_pago'
        verbose_name = "Tipo de Pago"
        verbose_name_plural = "Tipos de Pago"

class TipoVestimenta(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'tipos_vestimentas'
        verbose_name = "Tipo de Vestimenta"
        verbose_name_plural = "Tipos de Vestimentas"

class TipoPedido(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'tipos_pedidos'
        verbose_name = "Tipo de Pedido"
        verbose_name_plural = "Tipos de Pedidos"



""" Entidades débiles """
class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_entrada = models.DateField()
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'materiales'
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        db_table = 'clientes'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Vestimenta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    tipo_vestimenta = models.ForeignKey(TipoVestimenta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'vestimentas'
        verbose_name = "Vestimenta"
        verbose_name_plural = "Vestimentas"


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    cantidad = models.PositiveIntegerField()
    fecha_produccion = models.DateField()
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    vestimenta = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'producto'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Pedido(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    cantidad = models.PositiveIntegerField()
    fecha_pedido = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_pedido = models.ForeignKey(TipoPedido, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class Venta(models.Model):
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_venta = models.DateField()
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.PROTECT)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        db_table = 'venta'
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

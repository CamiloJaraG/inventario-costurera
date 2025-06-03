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

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        db_table = 'clientes'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Vestimenta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'vestimentas'
        verbose_name = "Vestimenta"
        verbose_name_plural = "Vestimentas"
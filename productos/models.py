from django.db import models

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

class TipoPago(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'tipos_pago'
        verbose_name = "Tipo de Pago"
        verbose_name_plural = "Tipos de Pago"
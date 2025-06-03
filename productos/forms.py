from django import forms
from productos.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

""" Formularios de tipos """
class TipoClienteForm(forms.ModelForm):
    class Meta:
        model = TipoCliente
        fields = ['tipo']
        labels = {
            'tipo': 'Tipo de Cliente',
        }
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo de cliente'}),
        }

class TipoMaterialForm(forms.ModelForm):
    class Meta:
        model = TipoMaterial
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del Tipo de Material',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del tipo de material'}),
        }

class TipoPagoForm(forms.ModelForm):
    class Meta:
        model = TipoPago
        fields = ['tipo']
        labels = {
            'tipo': 'Tipo de Pago',
        }
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo de pago'}),
        }

""" Formularios de entidades """
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de teléfono'}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'descripcion', 'cantidad', 'precio_unitario', 'fecha_entrada', 'tipo_material']
        labels = {
            'nombre': 'Nombre del Material',
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'precio_unitario': 'Precio Unitario',
            'fecha_entrada': 'Fecha de Entrada',
            'tipo_material': 'Tipo de Material',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del material'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio unitario'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha de entrada', 'type': 'date'}, format='%Y-%m-%d'),
            'tipo_material': forms.Select(attrs={'class': 'form-control'}),
        }

class VestimentaForm(forms.ModelForm):
    class Meta:
        model = Vestimenta
        fields = ['nombre', 'precio', 'cliente']
        labels = {
            'nombre': 'Nombre de la Vestimenta',
            'precio': 'Precio',
            'cliente': 'Cliente',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la vestimenta'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }


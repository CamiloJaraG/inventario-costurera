from django import forms
from productos.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
            'nombre': 'Nombre del Material',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del material'}),
        }

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

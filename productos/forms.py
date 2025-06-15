from django import forms
from productos.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su usuario'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))

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
#aca empieaza fomras pete
class TipoVestimentaForm(forms.ModelForm):
    class Meta:
        model = TipoVestimenta
        fields = ['tipo']
        labels = {
            'tipo': 'Tipo de Vestimenta',
        }
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo de vestimenta'}),
        }

class TipoPedidoForm(forms.ModelForm):
    class Meta:
        model = TipoPedido
        fields = ['tipo']
        labels = {
            'tipo': 'Tipo de Pedido',
        }
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo de pedido'}),
        }
#aca termina faorem pete
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
            'telefono': forms.TextInput(attrs={'class': 'solo-letras', 'placeholder': 'Ingrese su número de teléfono'}),
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

#aca empiz form 2s
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad', 'fecha_produccion', 'material', 'vestimenta']
        labels = {
            'nombre': 'Nombre del Producto',
            'cantidad': 'Cantidad',
            'fecha_produccion': 'Fecha de Produccion',
            'material': 'Material utilizado',
            'vestimenta':'Vestimenta asociada',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del producto'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad'}),
            'fecha_produccion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha de produccion', 'type': 'date'}, format='%Y-%m-%d'),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'vestimenta': forms.Select(attrs={'class': 'form-control'}),
        }


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'cantidad', 'fecha_pedido', 'producto', 'cliente', 'tipo_pedido']
        labels = {
            'nombre': 'Nombre del pedido',
            'cantidad': 'Cantidad',
            'fecha_pedido': 'Fecha del Pedido',
            'producto':'Producto asociado',
            'cliente':'Cliente asociado',
            'tipo_pedido': 'Tipo de pedido',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del pedido'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad'}),
            'fecha_pedido': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha de pedido', 'type': 'date'}, format='%Y-%m-%d'),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo_pedido': forms.Select(attrs={'class': 'form-control'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['descripcion', 'precio', 'fecha_venta', 'pedido', 'tipo_pago']
        labels = {
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'fecha_venta': 'Fecha de Venta',
            'pedido': 'Pedido Asociado',
            'tipo_pago': 'Tipo de Pago',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}),
            'fecha_venta': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha de venta', 'type': 'date'}, format='%Y-%m-%d'),
            'pedido': forms.Select(attrs={'class': 'form-control'}),
            'tipo_pago': forms.Select(attrs={'class': 'form-control'}),
        }
#aca termina cf 2
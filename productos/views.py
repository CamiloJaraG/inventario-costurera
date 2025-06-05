from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from productos.models import *
from productos.forms import *
from django.core.paginator import Paginator
import xlwt

# Permisos serán agregados más adelante

def inicio(request):
    data = {
        'titulo': 'Inicio',
    }
    return render(request, 'master.html', data)

def crearTipoCliente(request):
    formulario = TipoClienteForm()
    if request.method == 'POST':
        formulario = TipoClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de cliente creado exitosamente.')
    data = {
        'titulo': 'Crear tipo de cliente',
        'formulario': formulario,
        'ruta': '/productos/listartipoclientes/',
    }
    return render(request, 'formulario.html', data)

def listarTipoClientes(request):
    tipos_clientes = TipoCliente.objects.all()
    paginator = Paginator(tipos_clientes, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de tipos de cliente',
        'pageObj': pageObj,
    }
    return render(request, 'listas/tipos_clientes.html', data)

def editarTipoCliente(request, id):
    tipo_cliente = TipoCliente.objects.get(id=id)
    formulario = TipoClienteForm(instance=tipo_cliente)
    if request.method == 'POST':
        formulario = TipoClienteForm(request.POST, instance=tipo_cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de cliente editado exitosamente.')
    data = {
        'titulo': 'Editar tipo de cliente',
        'formulario': formulario,
        'ruta': '/productos/listartipoclientes/',
    }
    return render(request, 'formulario.html', data)

def eliminarTipoCliente(request, id):
    tipo_cliente = TipoCliente.objects.get(id=id)
    tipo_cliente.delete()
    messages.success(request, 'Tipo de cliente eliminado exitosamente.')
    return redirect('/productos/listartipoclientes/')

def crearTipoMaterial(request):
    formulario = TipoMaterialForm()
    if request.method == 'POST':
        formulario = TipoMaterialForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de material creado exitosamente.')
    data = {
        'titulo': 'Crear tipo de material',
        'formulario': formulario,
        'ruta': '/productos/listartipomateriales/',
    }
    return render(request, 'formulario.html', data)

def listarTipoMateriales(request):
    tipos_materiales = TipoMaterial.objects.all()
    paginator = Paginator(tipos_materiales, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de tipos de material',
        'pageObj': pageObj,
    }
    return render(request, 'listas/tipos_materiales.html', data)

def editarTipoMaterial(request, id):
    tipo_material = TipoMaterial.objects.get(id=id)
    formulario = TipoMaterialForm(instance=tipo_material)
    if request.method == 'POST':
        formulario = TipoMaterialForm(request.POST, instance=tipo_material)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de material editado exitosamente.')
    data = {
        'titulo': 'Editar tipo de material',
        'formulario': formulario,
        'ruta': '/productos/listartipomateriales/',
    }
    return render(request, 'formulario.html', data)

def eliminarTipoMaterial(request, id):
    tipo_material = TipoMaterial.objects.get(id=id)
    tipo_material.delete()
    messages.success(request, 'Tipo de material eliminado exitosamente.')
    return redirect('/productos/listartipomateriales/')

def crearMaterial(request):
    formulario = MaterialForm()
    if request.method == 'POST':
        formulario = MaterialForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Material creado exitosamente.')
    data = {
        'titulo': 'Crear material',
        'formulario': formulario,
        'ruta': '/productos/listarmateriales/',
    }
    return render(request, 'formulario.html', data)

def listarMateriales(request):
    materiales = Material.objects.all()
    paginator = Paginator(materiales, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de materiales',
        'pageObj': pageObj,
    }
    return render(request, 'listas/materiales.html', data)

def editarMaterial(request, id):
    material = Material.objects.get(id=id)
    formulario = MaterialForm(instance=material)
    if request.method == 'POST':
        formulario = MaterialForm(request.POST, instance=material)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Material editado exitosamente.')
    data = {
        'titulo': 'Editar material',
        'formulario': formulario,
        'ruta': '/productos/listarmateriales/',
    }
    return render(request, 'formulario.html', data)

def eliminarMaterial(request, id):
    material = Material.objects.get(id=id)
    material.delete()
    messages.success(request, 'Material eliminado exitosamente.')
    return redirect('/productos/listarmateriales/')

def crearCliente(request):
    formulario = ClienteForm()
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cliente creado exitosamente.')
    data = {
        'titulo': 'Crear cliente',
        'formulario': formulario,
        'ruta': '/productos/listarclientes/',
    }
    return render(request, 'formulario.html', data)

def listarClientes(request):
    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de clientes',
        'pageObj': pageObj,
    }
    return render(request, 'listas/clientes.html', data)

def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = ClienteForm(instance=cliente)
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cliente editado exitosamente.')
    data = {
        'titulo': 'Editar cliente',
        'formulario': formulario,
        'ruta': '/productos/listarclientes/',
    }
    return render(request, 'formulario.html', data)

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    messages.success(request, 'Cliente eliminado exitosamente.')
    return redirect('/productos/listarclientes/')

def crearVestimenta(request):
    formulario = VestimentaForm()
    if request.method == 'POST':
        formulario = VestimentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Vestimenta creada exitosamente.')
    data = {
        'titulo': 'Crear vestimenta',
        'formulario': formulario,
        'ruta': '/productos/listarvestimentas/',
    }
    return render(request, 'formulario.html', data)

def listarVestimentas(request):
    vestimentas = Vestimenta.objects.all()
    paginator = Paginator(vestimentas, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de vestimentas',
        'pageObj': pageObj,
    }
    return render(request, 'listas/vestimentas.html', data)

def editarVestimenta(request, id):
    vestimenta = Vestimenta.objects.get(id=id)
    formulario = VestimentaForm(instance=vestimenta)
    if request.method == 'POST':
        formulario = VestimentaForm(request.POST, instance=vestimenta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Vestimenta editada exitosamente.')
    data = {
        'titulo': 'Editar vestimenta',
        'formulario': formulario,
        'ruta': '/productos/listarvestimentas/',
    }
    return render(request, 'formulario.html', data)

def eliminarVestimenta(request, id):
    vestimenta = Vestimenta.objects.get(id=id)
    vestimenta.delete()
    messages.success(request, 'Vestimenta eliminada exitosamente.')
    return redirect('/productos/listarvestimentas/')

def crearTipoPago(request):
    formulario = TipoPagoForm()
    if request.method == 'POST':
        formulario = TipoPagoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de pago creado exitosamente.')
    data = {
        'titulo': 'Crear tipo de pago',
        'formulario': formulario,
        'ruta': '/productos/listartipopagos/',
    }
    return render(request, 'formulario.html', data)

def listarTipoPagos(request):
    tipos_pago = TipoPago.objects.all()
    paginator = Paginator(tipos_pago, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de tipos de pago',
        'pageObj': pageObj,
    }
    return render(request, 'listas/tipos_pago.html', data)

def editarTipoPago(request, id):
    tipo_pago = TipoPago.objects.get(id=id)
    formulario = TipoPagoForm(instance=tipo_pago)
    if request.method == 'POST':
        formulario = TipoPagoForm(request.POST, instance=tipo_pago)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de pago editado exitosamente.')
    data = {
        'titulo': 'Editar tipo de pago',
        'formulario': formulario,
        'ruta': '/productos/listartipopagos/',
    }
    return render(request, 'formulario.html', data)

def eliminarTipoPago(request, id):
    tipo_pago = TipoPago.objects.get(id=id)
    tipo_pago.delete()
    messages.success(request, 'Tipo de pago eliminado exitosamente.')
    return redirect('/productos/listartipopagos/')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from productos.models import Cliente, Vestimenta
from productos.forms import ClienteForm, VestimentaForm
from django.core.paginator import Paginator

# Permisos serán agregados más adelante

def inicio(request):
    data = {
        'titulo': 'Inicio',
    }
    return render(request, 'master.html', data)

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
    return redirect('/listas/listarclientes/')

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
        'ruta': '/listas/listarvestimentas/',
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
        'ruta': '/listas/listarvestimentas/',
    }
    return render(request, 'formulario.html', data)

def eliminarVestimenta(request, id):
    vestimenta = Vestimenta.objects.get(id=id)
    vestimenta.delete()
    messages.success(request, 'Vestimenta eliminada exitosamente.')
    return redirect('/listas/listarvestimentas/')
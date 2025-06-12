from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from productos.models import *
from productos.forms import *
from django.core.paginator import Paginator
import xlwt

def inicioSesion(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    formulario = LoginForm(request.POST)
    if request.method == 'POST' and formulario.is_valid():
        username = formulario.cleaned_data['username']
        password = formulario.cleaned_data['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        formulario = LoginForm()
    data = {
        'formulario': formulario,
    }
    return render(request, 'registration/login.html', data)

def cerrarSesion(request):
    auth_logout(request)
    return redirect('login')

@login_required()
def inicio(request):
    materiales_bajo_stock = Material.objects.filter(cantidad__lt=5)
    notificaciones = [f"{m.nombre} tiene bajo stock. ({m.cantidad} unidades)" for m in materiales_bajo_stock]
    data = {
        'titulo': 'Inicio',
        'notificaciones': notificaciones,
    }
    return render(request, 'master.html', data)

@permission_required('productos.add_tipocliente', login_url='login', raise_exception=True)
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

@permission_required('productos.view_tipocliente', login_url='login', raise_exception=True)
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

@permission_required('productos.change_tipocliente', login_url='login', raise_exception=True)
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

@permission_required('productos.delete_tipocliente', login_url='login', raise_exception=True)
def eliminarTipoCliente(request, id):
    tipo_cliente = TipoCliente.objects.get(id=id)
    tipo_cliente.delete()
    messages.success(request, 'Tipo de cliente eliminado exitosamente.')
    return redirect('/productos/listartipoclientes/')

@permission_required('productos.add_tipomaterial', login_url='login', raise_exception=True)
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

@permission_required('productos.view_tipomaterial', login_url='login', raise_exception=True)
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

@permission_required('productos.change_tipomaterial', login_url='login', raise_exception=True)
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

@permission_required('productos.delete_tipomaterial', login_url='login', raise_exception=True)
def eliminarTipoMaterial(request, id):
    tipo_material = TipoMaterial.objects.get(id=id)
    tipo_material.delete()
    messages.success(request, 'Tipo de material eliminado exitosamente.')
    return redirect('/productos/listartipomateriales/')

#aca empieza codigo pete
@permission_required('productos.add_tipovestimenta', login_url='login', raise_exception=True)
def crearTipoVestimenta(request):
    formulario = TipoVestimentaForm()
    if request.method == 'POST':
        formulario = TipoVestimentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de Vestimenta creado exitosamente.')
    data = {
        'titulo': 'Crear tipo de vestimenta',
        'formulario': formulario,
        'ruta': '/productos/listartipovestimentas/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.view_tipovestimenta', login_url='login', raise_exception=True)
def listarTipoVestimentas(request):
    tipos_vestimentas = TipoVestimenta.objects.all()
    paginator = Paginator(tipos_vestimentas, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de tipos de vestimenta',
        'pageObj': pageObj,
    }
    return render(request, 'listas/tipos_vestimentas.html', data)

@permission_required('productos.change_tipovestimenta', login_url='login', raise_exception=True)
def editarTipoVestimenta(request, id):
    tipo_vestimenta = TipoVestimenta.objects.get(id=id)
    formulario = TipoVestimentaForm(instance=tipo_vestimenta)
    if request.method == 'POST':
        formulario = TipoVestimentaForm(request.POST, instance=tipo_vestimenta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de vestimenta editado exitosamente.')
    data = {
        'titulo': 'Editar tipo de vestimenta',
        'formulario': formulario,
        'ruta': '/productos/listartipovestimentas/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.delete_tipovestimenta', login_url='login', raise_exception=True)
def eliminarTipoVestimenta(request, id):
    tipo_vestimenta = TipoVestimenta.objects.get(id=id)
    tipo_vestimenta.delete()
    messages.success(request, 'Tipo de vestimenta eliminado exitosamente.')
    return redirect('/productos/listartipovestimentas/')
#aca termina codigo pete

@permission_required('productos.add_material', login_url='login', raise_exception=True)
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

@permission_required('productos.view_material', login_url='login', raise_exception=True)
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

@permission_required('productos.change_material', login_url='login', raise_exception=True)
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

@permission_required('productos.delete_material', login_url='login', raise_exception=True)
def eliminarMaterial(request, id):
    material = Material.objects.get(id=id)
    material.delete()
    messages.success(request, 'Material eliminado exitosamente.')
    return redirect('/productos/listarmateriales/')

@permission_required('productos.add_cliente', login_url='login', raise_exception=True)
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

@permission_required('productos.view_cliente', login_url='login', raise_exception=True)
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

@permission_required('productos.change_cliente', login_url='login', raise_exception=True)
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

@permission_required('productos.delete_cliente', login_url='login', raise_exception=True)
def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    messages.success(request, 'Cliente eliminado exitosamente.')
    return redirect('/productos/listarclientes/')

@permission_required('productos.add_vestimenta', login_url='login', raise_exception=True)
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

@permission_required('productos.view_vestimenta', login_url='login', raise_exception=True)
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

@permission_required('productos.change_vestimenta', login_url='login', raise_exception=True)
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

@permission_required('productos.delete_vestimenta', login_url='login', raise_exception=True)
def eliminarVestimenta(request, id):
    vestimenta = Vestimenta.objects.get(id=id)
    vestimenta.delete()
    messages.success(request, 'Vestimenta eliminada exitosamente.')
    return redirect('/productos/listarvestimentas/')

@permission_required('productos.add_tipopago', login_url='login', raise_exception=True)
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

@permission_required('productos.view_tipopago', login_url='login', raise_exception=True)
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

@permission_required('productos.change_tipopago', login_url='login', raise_exception=True)
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

@permission_required('productos.delete_tipopago', login_url='login', raise_exception=True)
def eliminarTipoPago(request, id):
    tipo_pago = TipoPago.objects.get(id=id)
    tipo_pago.delete()
    messages.success(request, 'Tipo de pago eliminado exitosamente.')
    return redirect('/productos/listartipopagos/')
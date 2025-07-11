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
    
    data = {
        'titulo': 'Inicio',
        'total_productos': Producto.objects.count(),
        'total_materiales': Material.objects.count(),
        'total_clientes': Cliente.objects.count(),
        'total_ventas': Venta.objects.count(),
    }
    return render(request, 'master.html', data)

#tipocliente
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

#tipomaterial
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


@permission_required('productos.add_tipopedido', login_url='login', raise_exception=True)
def crearTipoPedido(request):
    formulario = TipoPedidoForm()
    if request.method == 'POST':
        formulario = TipoPedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de Pedido creado exitosamente.')
    data = {
        'titulo': 'Crear tipo de pedido',
        'formulario': formulario,
        'ruta': '/productos/listartipopedidos/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.view_tipopedido', login_url='login', raise_exception=True)
def listarTipoPedidos(request):
    tipos_pedidos = TipoPedido.objects.all()
    paginator = Paginator(tipos_pedidos, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de tipos de pedidos',
        'pageObj': pageObj,
    }
    return render(request, 'listas/tipos_pedidos.html', data)

@permission_required('productos.change_tipopedido', login_url='login', raise_exception=True)
def editarTipoPedido(request, id):
    tipo_pedido = TipoPedido.objects.get(id=id)
    formulario = TipoPedidoForm(instance=tipo_pedido)
    if request.method == 'POST':
        formulario = TipoPedidoForm(request.POST, instance=tipo_pedido)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de pedido editado exitosamente.')
    data = {
        'titulo': 'Editar tipo de pedido',
        'formulario': formulario,
        'ruta': '/productos/listartipopedidos/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.delete_tipopedido', login_url='login', raise_exception=True)
def eliminarTipoPedido(request, id):
    tipo_pedido = TipoPedido.objects.get(id=id)
    tipo_pedido.delete()
    messages.success(request, 'Tipo de pedido eliminado exitosamente.')
    return redirect('/productos/listartipopedidos/')

# material
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

#cliente
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

#vestimenta
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

@permission_required('productos.add_producto', login_url='login', raise_exception=True)
def crearProducto(request):
    formulario = ProductoForm()
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto creado exitosamente.')
    data = {
        'titulo': 'Crear Producto',
        'formulario': formulario,
        'ruta': '/productos/listarproductos/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.view_producto', login_url='login', raise_exception=True)
def listarProductos(request):
    producto = Producto.objects.all()
    paginator = Paginator(producto, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de producto',
        'pageObj': pageObj,
    }
    return render(request, 'listas/productos.html', data)

@permission_required('productos.change_producto', login_url='login', raise_exception=True)
def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(instance=producto)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto editado exitosamente.')
    data = {
        'titulo': 'Editar Producto',
        'formulario': formulario,
        'ruta': '/productos/listarproductos/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.delete_producto', login_url='login', raise_exception=True)
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('/productos/listarproductos/')


@permission_required('productos.add_pedido', login_url='login', raise_exception=True)
def crearPedido(request):
    formulario = PedidoForm()
    if request.method == 'POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Pedido creado exitosamente.')
    data = {
        'titulo': 'Crear Pedido',
        'formulario': formulario,
        'ruta': '/productos/listarpedidos/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.view_pedido', login_url='login', raise_exception=True)
def listarPedidos(request):
    pedido = Pedido.objects.all()
    paginator = Paginator(pedido, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de pedidos',
        'pageObj': pageObj,
    }
    return render(request, 'listas/pedidos.html', data)

@permission_required('productos.change_pedido', login_url='login', raise_exception=True)
def editarPedido(request, id):
    pedido = Pedido.objects.get(id=id)
    formulario = PedidoForm(instance=pedido)
    if request.method == 'POST':
        formulario = PedidoForm(request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Pedido editado exitosamente.')
    data = {
        'titulo': 'Editar Pedido',
        'formulario': formulario,
        'ruta': '/productos/listarpedidos/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.delete_pedido', login_url='login', raise_exception=True)
def eliminarPedido(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    messages.success(request, 'Pedido eliminado exitosamente.')
    return redirect('/productos/listarpedidos/')


@permission_required('productos.add_venta', login_url='login', raise_exception=True)
def crearVenta(request):
    formulario = VentaForm()
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Venta creada exitosamente.')
    data = {
        'titulo': 'Crear Venta',
        'formulario': formulario,
        'ruta': '/productos/listarventas/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.view_venta', login_url='login', raise_exception=True)
def listarVentas(request):
    venta = Venta.objects.all()
    paginator = Paginator(venta, 10) 
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
        'titulo': 'Lista de ventas',
        'pageObj': pageObj,
    }
    return render(request, 'listas/ventas.html', data)

@permission_required('productos.change_venta', login_url='login', raise_exception=True)
def editarVenta(request, id):
    venta = Venta.objects.get(id=id)
    formulario = VentaForm(instance=venta)
    if request.method == 'POST':
        formulario = VentaForm(request.POST, instance=venta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Venta editada exitosamente.')
    data = {
        'titulo': 'Editar Venta',
        'formulario': formulario,
        'ruta': '/productos/listarventas/',
    }
    return render(request, 'formulario.html', data)

@permission_required('productos.delete_venta', login_url='login', raise_exception=True)
def eliminarVenta(request, id):
    venta = Venta.objects.get(id=id)
    venta.delete()
    messages.success(request, 'Venta eliminada exitosamente.')
    return redirect('/productos/listarventas/')
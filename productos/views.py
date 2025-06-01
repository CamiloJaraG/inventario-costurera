from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    data = {
        'titulo': 'Inicio',
        'message': 'Bienvenido al sistema de gestión de inventario.',
    }
    return render(request, 'master.html', data)


from productos.models import Material

def notificaciones_context(request):
    notificaciones = []

    if request.user.is_authenticated:
        materiales = Material.objects.all()
        for material in materiales:
            if material.cantidad == 0:
                notificaciones.append({
                    'mensaje': f"{material.nombre} está <strong>agotado</strong>.",
                    'icono': 'fa-circle-exclamation text-danger'
                })
            elif material.cantidad < 15:
                notificaciones.append({
                    'mensaje': f"{material.nombre} tiene <strong>bajo stock</strong>. ({material.cantidad} unidades)",
                    'icono': 'fa-triangle-exclamation text-warning'
                })

    return {'notificaciones': notificaciones}

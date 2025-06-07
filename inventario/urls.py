from django.contrib import admin
from django.urls import include, path
from productos.views import inicio
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(inicio), name='inicio'),
    path('productos/', include('productos.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
]
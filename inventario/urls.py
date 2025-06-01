from django.contrib import admin
from django.urls import include, path
from productos.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('productos/', include('productos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

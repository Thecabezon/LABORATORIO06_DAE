from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),  # Agrega esta línea
    path('boletin/', include('boletin.urls')),  # Agrega esta línea para incluir las URLs de la app boletin
]
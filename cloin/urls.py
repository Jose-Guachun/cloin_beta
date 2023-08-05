"""cloin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#Importacion de settings y static para generar ruta en templates
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    # Urls de apps creadas
    path('', include(('inventario.urls', 'inventario'), namespace='inventario')),
    path('users/', include(('users.urls', 'users'), namespace='users'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

#Importacion de vistas
from inventario import adm_inventario

urlpatterns=[
    # managment
    path(
        route='adm_inventario/<str:action>',
        view=adm_inventario.ViewSet.as_view(),
        name='adm_inventario',
    ),

]

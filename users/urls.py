from django.urls import path

#Importacion de vistas
from users.acceso_sistema import LoginView

urlpatterns=[
    # managment
    path(
        route='login',
        view=LoginView.as_view(),
        name='login',
    ),

]

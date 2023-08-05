#django
from django.db import models
from django.conf import settings

#utilities
from utils.models import ModeloBase
from django.core import validators
from cloin.validators import vcedula, SoloNumeros, SoloLetras


from users.models import User
# from posts.models import Project
# from iteractions.models import Relationship

def ruta(instance, file_name):
    route='{}/{}/{}/{}'.format('users',instance.user.email,'profile_picture',file_name)
    return route

GENERO=(
    (1, u'Masculino'),
    (2, u'Femenino'),
)
TIPO_PERFIL=(
    (1, u'Cliente'),
    (2, u'Administrativo'),
    (3, u'Gerente'),
)

class Person(ModeloBase):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    country=models.ForeignKey('users.Country', on_delete=models.CASCADE, blank=True, null=True)
    province=models.ForeignKey('users.Province', on_delete=models.CASCADE, blank=True, null=True)
    city=models.ForeignKey('users.City', on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField('Nombres', max_length=30, validators=[validators.MinLengthValidator(3)])
    last_name_first= models.CharField('Primer Apellido', max_length=30,validators=[validators.MinLengthValidator(3)])
    last_name_second = models.CharField('Segundo Apellido', max_length=30,validators=[validators.MinLengthValidator(3)], default='')
    dni=models.CharField(max_length=10, validators=[validators.MinLengthValidator(10), vcedula], blank=True)
    gender=models.IntegerField(choices=GENERO, null=True, blank=True, verbose_name="Genero")
    birth_date=models.DateField(blank=True, null=True)
    biography=models.TextField(blank=True, null=True)
    phone_number=models.CharField(max_length=20, validators=[validators.MinLengthValidator(10), SoloNumeros], blank=True)
    picture=models.ImageField(upload_to=ruta,blank=True, null=True,)
    # otros campos de información personal

    def __str__(self):
        return f"{self.first_name} {self.last_name_first}"
class Profile(ModeloBase):
    #profile model
    person = models.ForeignKey(Person,on_delete=models.CASCADE, verbose_name="Persona asignada al perfil")
    tipo=models.IntegerField(choices=TIPO_PERFIL, default=1, verbose_name="Tipo de perfil de usuario")

    def __str__(self):
        #return username
        return str(self.person)


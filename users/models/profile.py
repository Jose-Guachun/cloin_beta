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
class Profile(ModeloBase):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    user=models.OneToOneField('users.User', on_delete=models.CASCADE,)
    city=models.ForeignKey('users.City', on_delete=models.CASCADE, blank=True, null=True)
    dni=models.CharField(max_length=10, validators=[validators.MinLengthValidator(10), vcedula], blank=True)
    gender=models.IntegerField(choices=GENERO, null=True, blank=True, verbose_name="Genero")
    birth_date=models.DateField(blank=True, null=True)
    biography=models.TextField(blank=True, null=True)
    phone_number=models.CharField(max_length=20, validators=[validators.MinLengthValidator(10), SoloNumeros], blank=True)
    education_level=models.CharField(max_length=50, blank=True)
    work_area=models.CharField(max_length=100, blank=True, validators=[validators.MinLengthValidator(4)], )
    picture=models.ImageField(upload_to=ruta,blank=True, null=True,)

    def __str__(self):
        #return username
        return str(self.user)


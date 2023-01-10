from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


# Create your models here.
class administrators(models.Model):
    ROL=[
        ('A','Administrador'),
        ('S','SuperAdministrador')
    ]
    id_administrador=models.BigAutoField(primary_key=True)
    nombre_administrador=models.TextField(max_length=100)
    password_administrador=models.TextField(max_length=100)
    rol_administrador=models.CharField(max_length=100,choices=ROL,default=ROL[0])
    id_user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_administrador

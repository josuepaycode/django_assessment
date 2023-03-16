from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

# Create your models here.
class Administrators(AbstractUser):
    USER_TYPE = (
        ('administrador','Administrador'),
        ('super_administrador','Super Administrador')
    )
    name = models.CharField(max_length=50, unique=True)
    username = None
    rol = models.CharField(max_length=25, choices=USER_TYPE, null=False, blank=False)

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = [ "password", "rol"]


    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.name


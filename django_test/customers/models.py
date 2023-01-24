from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    paternal_surname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

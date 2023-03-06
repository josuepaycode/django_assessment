from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    """Customer Model"""
    name = models.CharField(max_length=250)
    paternal_surname = models.CharField(max_length=250)
    email = models.EmailField(max_length=300, unique=True)

    def __str__(self) -> str:
        return self.name


class CustomerPayment(models.Model):
    """Customer Payment Model"""
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    customer_id = models.ForeignKey(
        'Customer', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.product_name} {self.customer_id}"


class Administrator(models.Model):
    """Admin Model"""
    class AdminRol(models.TextChoices):
        """AdminRol Choice Class"""
        ADMINISTRATOR = 'administrator'
        SUPER_ADMINISTRATOR = 'super_administrator'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    rol = models.CharField(max_length=250, choices=AdminRol.choices)

    def __str__(self) -> str:
        return self.name

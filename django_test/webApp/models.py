from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
import datetime

import random

# Create your models here.

class Customers(models.Model):
    """ Modelo de clientes """
    name =  models.CharField(max_length=50)
    paternal_surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

@receiver(post_save, sender=Customers)
def payments_customers_dummy_generator(sender, instance, created, **kwargs):
    """ Generador para registros dummy de PaymentsCustomers al crear Customer """

    n = random.randint(0,10) #Numero de productos a generar
    if created:
        instance.created_at = datetime.datetime.now()
        instance.save()
        for i in range(1,n):
            quantity = random.randint(0,20)
            amount = random.uniform(0,100)
            
            product = "Product {}".format(i)
            p = PaymentsCustomers(amount=amount, customer=instance, product_name=product, quantity=quantity)
            p.save()

class PaymentsCustomers(models.Model):
    """ Modelo para pago de clientes """
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.ForeignKey("Customers", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Administrators(models.Model):
    """ Modelo para adrminsitradores """
    """ 
        *** CREDENCIALES ***
        
        -SUPERADMIN{
            name: superadmin
            password: password
        }
        -ADMIN{
            name: admin
            password: passwordadmin
        }
    """
    ROLES = (
        ('A','administrator'),
        ('S','super_administrator')
    )
    name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=50)
    rol = models.CharField(max_length=50, choices=ROLES)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    USERNAME_FIELD = 'name'
    EMAIL_FIELD = ''
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name
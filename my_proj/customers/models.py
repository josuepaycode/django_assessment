from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=20)
    paternal_surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return "%s %s %s" % (self.name,self.paternal_surname,self.email)

    def get_absolute_url(self):
        return reverse('customer_edit', kwargs={'pk': self.pk})

class Payments_Customers(models.Model):
    amount = models.FloatField()
    customer_id =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name  = models.CharField(max_length=20)
    quantity = models.IntegerField()
    #
    def __str__(self):
        return "%f %i %s %i" % (self.amount,self.customer_id,self.product_name,self.quantity)


ADMIN = "ADMIN"
SUPERADMIN="SUPERADMIN"

ROLS_CHOICES= (
	(ADMIN,"Admin"),
	(SUPERADMIN,"SuperAdmin")
	)

class Admin(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    rol = models.CharField(
	max_length= 10,
	choices=ROLS_CHOICES,
	default=ADMIN)

    def __str__(self):
        return "%s %s" % (self.name,self.rol)

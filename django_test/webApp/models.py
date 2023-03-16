from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Customer(models.Model):
    name =  models.CharField( max_length=50, null=False, blank= False)
    paternal_surname =  models.CharField(max_length=50, null=False, blank=False)
    email =  models.EmailField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return f"{self.name} {self.paternal_surname}"

class PaymentCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    amount =  models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False)
    product_name = models.CharField(max_length=50, null=False, blank=False)
    quantity =  models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.product_name






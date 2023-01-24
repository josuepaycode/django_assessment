import random
from django.db import models
from faker import Faker

from payments.models import Payment

fake = Faker()

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    paternal_surname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
    def save(self, *args, **kwargs):
        _is_new = False
        if self._state.adding:
            _is_new = True

        super().save(*args, **kwargs)

        if _is_new:
            for i in range(0, 10):
                Payment.objects.create(
                    amount=fake.pyfloat(left_digits=3, right_digits=3), 
                    product_name=fake.name(),
                    quantity=fake.pyint(),
                    customer=self
                )

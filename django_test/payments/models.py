from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.FloatField(default=0.0, null=True, blank=True)
    product_name = models.CharField(max_length=200, unique=True)
    quantity = models.PositiveIntegerField()
    customer_id = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)

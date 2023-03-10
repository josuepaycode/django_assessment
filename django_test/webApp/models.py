from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=150)
    paternal_surname = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.name} {self.paternal_surname}'
    

class PaymentCustomer(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='payments')
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Payment Customer'
        verbose_name_plural = 'Payments Customers'

    def __str__(self):
        return f'{self.customer.name} {self.customer.paternal_surname} - {self.amount}'
    

class Administrator(models.Model):
    ROLES = [
        ('administrator','Administrator'),
        ('super_administrator', 'Super Administrator')
    ]
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)
    rol = models.CharField(max_length=20, choices=ROLES)

    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

    def __str__(self):
        return self.name


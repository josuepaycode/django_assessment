from django.db import models
from customers.models import customers
# Create your models here.

class payments(models.Model):
    id_pago=models.BigAutoField(primary_key=True)
    cantidad_pago=models.TextField(max_length=10)
    id_cliente=models.ForeignKey(customers,on_delete=models.CASCADE)
    producto=models.TextField(max_length=30)
    cantidad_producto=models.TextField(max_length=10)
    fecha_pago=models.DateField(auto_now_add=True)

    @property
    def cliente_id(self):
        return self.id_cliente.id_customer
    
    @property
    def nombre_cliente(self):
        nombre=self.id_cliente.nombre_cliente + self.id_cliente.apellido_cliente
        return nombre
        
    def __str__(self):
        return self.cantidad_pago



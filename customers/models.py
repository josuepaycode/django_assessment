from django.db import models

# Create your models here.

class customers(models.Model):
  id_customer=models.BigAutoField(primary_key=True)
  nombre_cliente=models.TextField(max_length=10)
  apellido_cliente=models.TextField(max_length=10)
  correo=models.EmailField(unique=True)
  class Meta:
    unique_together=['nombre_cliente','apellido_cliente','correo']
  def __str__(self):
    salida=str(self.id_customer)+' - '+ self.nombre_cliente + ' ' + self.apellido_cliente
    return salida
  

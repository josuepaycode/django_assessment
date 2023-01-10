from django import forms
from .models import customers

class nuevoclienteform(forms.ModelForm):
  class Meta:
    model=customers
    fields='__all__'
    widgets={
      'nombre_cliente':forms.TextInput(attrs={'class':'form-control'}),
      'apellido_cliente':forms.TextInput(attrs={'class':'form-control'}),
      'correo':forms.TextInput(attrs={'class':'form-control'})
    }
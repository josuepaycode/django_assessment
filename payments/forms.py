from django import forms
from .models import payments

class newpaymentform(forms.ModelForm):

    class Meta:
        model=payments
        fields='__all__'
        widgets={
            'cantidad_pago':forms.TextInput(attrs={'class':'form-control'}),
            'producto':forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_producto':forms.TextInput(attrs={'class':'form-control'}),
            'id_cliente':forms.Select(attrs={'class':'select'}),
        }

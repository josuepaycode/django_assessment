from django import forms
from .models import administrators

class loginform(forms.Form):
    nombre_login=forms.CharField(max_length=200)
    password_login=forms.CharField(max_length=200)

    def clean(self):
        username=self.cleaned_data.get('nombre_login')
        password=self.cleaned_data.get('password_login')
        user_login=administrators.objects.filter(nombre_administrador=username).filter(password_administrador=password)
        if not user_login:
            raise forms.ValidationError('usuario no encontrado')
        return self.cleaned_data

    def login(self,request):
        nombre_login=self.cleaned_data.get('nombre_login')
        password_login=self.cleaned_data.get('password_login')
        user_login=administrators.objects.filter(nombre_administrador=nombre_login).filter(password_administrador=password_login)
        return user_login
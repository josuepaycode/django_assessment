from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response



def login_user(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            context = {'error': 'wrong credentials'}  # to display error?
            return render(request, 'login.html', {'context': context})
        
def logout_user(request):
    logout(request)
    return redirect('login')


# REST Services 


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = {}
        try:
            code =200  
            serializer = self.serializer_class(
                data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'token': token.key,
            }
        except Exception as e:
            response = {"error": "Usuario y/o contraseña invalida"}
        return Response(response, status=code)
    
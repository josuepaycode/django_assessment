from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from .forms import loginform

# Create your views here.

def login_request(request):
    page=loader.get_template('useraccess/login.html')   
    form=AuthenticationForm()
    if request.method == 'GET':
        context={'form':form}
        return HttpResponse(page.render(context,request))
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is None:
            context={'form':form,'error':'usuario o pasword invalidos'}
            return HttpResponse(page.render(context,request))
        user_session=login(request,user)
        print(user_session)
        return redirect('/')
        
@login_required    
def logout_request(request):
    logout(request)
    return redirect('/')

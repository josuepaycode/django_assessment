from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/app/login')
def main(request):
    if request.user.is_authenticated:
        return redirect('app/')
    else:
        return redirect('app/login/')

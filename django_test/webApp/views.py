from django.shortcuts import render, redirect

from webApp.forms import GenerateLoginForm
from webApp.models import Administrators


# Create your views here.
def login(request):
    form = GenerateLoginForm()
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': form,
        })
    else:
        form = GenerateLoginForm(request.POST or None)
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                return redirect('dashboard/' + str(user.id))
        return render(request, 'login.html', {
            'form': form,
        })


def dashboard(request, id):
    user = Administrators.objects.filter(id=id).first()
    if request.method == 'GET':
        return render(request, 'dashboard.html', {
            'user': user
        })

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .models import payments
from .forms import newpaymentform

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def paymentsview(request):
    page=loader.get_template('payments/payments.html')
    pagos=payments.objects.all().values()
    pagos_obj=payments.objects.all()
    context={'pagos':pagos,'objetos':pagos_obj}
    return HttpResponse(page.render(context,request))

@login_required
def newpayment(request):
    page=loader.get_template('payments/newpayment.html')
    form=newpaymentform
    if request.method =='POST':
        form=newpaymentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/payments')
    context={'form':form}
    return HttpResponse(page.render(context,request))

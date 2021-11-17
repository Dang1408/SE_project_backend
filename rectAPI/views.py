import django
from django import forms
from django.shortcuts import redirect, render

from rectAPI.models import order

from .forms import OrderForm

# Create your views here.
def index(request):
    return render(request, "first.html")

def payment(request):
    return render(request, "payment.html")

def order(request):

    if request.method=="POST":
        print("this is post")
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        mobilephone = request.POST['phone']
        totalofcost = request.POST.get('amount',False)
        notehere = request.POST['note']
        ins = order(first_name = f_name, last_name = l_name, phone = mobilephone , totalcost =totalofcost, note =notehere)
        ins.save()
    return render(request,'payment.html')

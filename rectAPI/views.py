from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "first.html")

def payment(request):
    return render(request, "payment.html")
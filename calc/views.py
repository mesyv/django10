from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePage(request):
    return render(request, 'calc/home.html')

def kcalCalc(request):
    return render(request, 'calc/kcalcalc.html')

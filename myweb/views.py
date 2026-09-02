

from django.shortcuts import render



def home(request):
    return render(request,'product.html',)

def product(request):
    pass
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')
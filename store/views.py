from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    template_name = 'store/home.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name, context)

def cart(request):
    template_name = 'store/cart.html'
    context = {}
    return render(request, template_name, context)

def checkout(request):
    template_name = 'store/checkout.html'
    context = {}
    return render(request, template_name, context)


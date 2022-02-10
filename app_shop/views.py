from itertools import product
from django.shortcuts import render
from .models import Product

def home(request):
    ctx = {
        'product_list': Product.objects.all()
    }
    return render(request, 'home.html', ctx)

def product_detail(request, pk):
    ctx = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'product_detail.html', ctx)

def product_list(request):
    ctx = {
        'product_list': Product.objects.all()
    }
    return render(request, 'product_list.html', ctx)
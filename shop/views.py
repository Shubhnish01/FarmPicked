from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def Shopss(request):
    products = Product.objects.all()
    params = {"product": products}
    return render(request, "FreshFruits.html", params)


def tracker(request):
    return HttpResponse("this is tracer")
    # return render(request, 'FreshFruits.html')


def search(request):
    return render(request, "FreshFruits.html")


def productView(request):
    return render(request, "FreshFruits.html")

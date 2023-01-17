from django.shortcuts import render
from .models import UserDetails ,Product
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    sarees = Product.objects.filter(catry="Sarees")
    dresses = Product.objects.filter(catry="Dresses")
    bc = Product.objects.filter(catry="Baby Costumes")
    gc = Product.objects.filter(catry="Girls Costumes")
    
    print(gc.count())
    context = {
        'sarees' : sarees,
        'dresses':dresses,
        'bc':bc,
        "gc":gc
    }
    return render(request, "home.html",context=context)

def search(request,val):
    
    products = Product.objects.all()
    context = {
    'products':products,
    'c' : products.count(),
    's' : val
    }
    return render(request, "search.html",context=context)

def detail(request,id):
    product = Product.objects.get(id=id)
    seller_details = UserDetails.objects.get(user=product.seller)
    yt = str(product.yt_link)
    yt = yt.replace('watch?v=', 'embed/')
    data = {
        "product":product,
        'seller':seller_details.name,
        'pic':seller_details.profile.url,
        'yt':yt
    }
    return render(request, "detail.html",data)


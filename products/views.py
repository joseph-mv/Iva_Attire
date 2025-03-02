from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,'index.html')

def list_products(req):
    return render(req,'list_products.html')

def detail_product(req):
    return render(req,'product_detail.html')
    

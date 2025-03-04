from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(req):
    featured_products=Product.objects.order_by('-priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(req,'index.html',context)

def list_products(req):
    page=1
    if req.GET:
        page=req.GET.get('page',1)
    products=Product.objects.order_by('-priority')
    product_paginator=Paginator(products,4)
    product_list=product_paginator.get_page(page)
    return render(req,'list_products.html',{'products':product_list})

def detail_product(req,pk):
    product=Product.objects.get(id=pk)
    return render(req,'product_detail.html',{'product':product})
    

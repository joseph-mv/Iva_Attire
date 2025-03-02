from django.shortcuts import render

# Create your views here.

def show_cart(req):
    return render(req,'cart.html')

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Customer
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def show_account(req):
    context={}
    try:  
        if req.POST and 'register' in req.POST:
            context['register']=True
            username=req.POST.get('username')
            email=req.POST.get('email')
            address=req.POST.get('address')
            phone=req.POST.get('phone')
            password=req.POST.get('password')
            # create user account
            user=User.objects.create_user(username=username,email=email ,password=password)            
            
            # crete Customer
            customer=Customer.objects.create(user=user,phone=phone,address=address)
            print(customer)
            messages.success(req,'User registered successfully')

    except Exception as e:
        error_msg=str(e)
        print(error_msg)
        messages.error(req,'Duplicate username or Invalid credentials')

    if req.POST and 'login' in req.POST:
        context['register']=False
        username=req.POST.get('username')
        password=req.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,'Invalid credentials')
  
    return render(req,'account.html',context)


def sign_out(req):
    logout(req)
    return redirect('home')
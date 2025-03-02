from django.shortcuts import render

# Create your views here.
def show_account(req):
    return render(req,'account.html')
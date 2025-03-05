from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import  login_required

# Create your views here.
@login_required(login_url='/customer/')
def show_cart(req):
    user=req.user
    customer=user.user_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

    print( cart_obj.id, cart_obj.order_status)

    context={'cart':cart_obj.added_items.all()}
    return render(req,'cart.html',context)

@login_required(login_url='/customer/')
def add_to_cart(req):
    if req.POST:
        user=req.user
        customer=user.user_profile
        quantity=req.POST.get('quantity')
        product_id=req.POST.get('product_id')
        product=Product.objects.get(id=product_id)
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        order_item,created=OrderedItem.objects.get_or_create(
            product=product,owner=cart_obj
        )
        if created:
            order_item.quantity=quantity
            order_item.save()
        else:
            order_item.quantity+=int(quantity)
            order_item.save()
        return redirect('cart')

@login_required(login_url='/customer/')
def remove_item(req ,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:

        item.delete()
    return redirect('cart')

@login_required(login_url='/customer/')
def check_out(req):
    try:
        if req.POST:
            user=req.user
            customer=user.user_profile
            total=req.POST.get('total')
            order_obj=Order.objects.get(
                 owner=customer,
            order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                messages.success(req,"Your Order is placed")
            else:
                messages.error(req,"unable to processed")
            print(order_obj.id,order_obj.order_status)
        return redirect('cart')
    except Exception as e:
        messages.error(req,"unable to processed")
    
def view_orders(req):
    user=req.user
    customer=user.user_profile
    orders=customer.orders.exclude(order_status=Order.CART_STAGE)
    return render(req,'orders.html',{'orders':orders})





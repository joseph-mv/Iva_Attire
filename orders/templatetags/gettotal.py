from django import template

register = template.Library()

@register.simple_tag(name='gettotal')
def gettotal(cart):
    total=0
    for item in cart:
        total+=item.product.price*item.quantity

    return total





from django import template

register = template.Library()

@register.simple_tag(name='order_status')
def order_status(status_num):
    status={
    1: 'CONFIRMED',
    2: 'PROCESSED',
    3:' DELIVERED',
    4: 'REJECTED'
    }
    return status[status_num]
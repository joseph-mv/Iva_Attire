from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_cart, name='cart' ),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<pk>',views.remove_item,name='remove_item'),
    path('check_out/',views.check_out,name='check_out'),
    path('view_orders/',views.view_orders,name='view_orders'),
]
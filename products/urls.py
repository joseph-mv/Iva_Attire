from django.urls import path
from . import views
urlpatterns = [
    path('',views.index ),
    path('products/',views.list_products , name='list_products'),
    path('product_details',views.detail_product ,name='detail_product')

]
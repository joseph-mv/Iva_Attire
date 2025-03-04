from django.urls import path
from . import views
urlpatterns = [
    path('customer/',views.show_account ),
    path('logout/',views.sign_out)
    

]
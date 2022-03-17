from django.urls import path 
from . import views  

app_name = 'order'  

urlpatterns = [
    path('addtoshopcart/', views.addtoshopcart, name='addtoshopcart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('updatequantity/',views.updatequantity,name='updatequantity'),
    path('deletefromcart/<str:id>', views.deletefromcart, name='deletefromcart'),
    path('checkout/', views.checkout, name= 'checkout'),
    path('placeorder/', views.placeorder, name ='placeorder'),
    path('ordercompleted/', views.ordercompleted, name='ordercompleted'),
]

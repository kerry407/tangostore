from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('products/<str:id>/', views.prod_list, name='prod_list'),
    path('product-details/<str:id>/', views.prod_detail, name='prod_detail' ),
    path('contact/', views.contact, name='contact'),
]

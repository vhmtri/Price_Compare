from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name='product_list'),
    path('product-search/', views.product_search, name='product_search'),
    path('base/', views.base, name='base'),
    path('products/<path:product_name>/', views.product_detail, name='product_detail'),
    #re_path(r'^products/(?P<product_name>[\w\s\-/]+)$', views.product_detail, name='product_detail')
]
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

app_name = "shop" 

urlpatterns = [

    # The home page
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('search_category', views.search_category, name='search_category'),
    path('search_product', views.search_product, name='search_product'),
    path('search_order', views.search_order, name='search_order'),
    path('search_customer', views.search_customer, name='search_customer'),
    

    #shop
    path('seller', views.index, name='seller'),
    path('shop', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:product_id>/', views.product_update, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('<slug:category_slug>/', views.customer_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/update/<int:category_id>/', views.category_update, name='category_update'),
    path('category/delete/<int:category_id>/', views.category_delete, name='category_delete'),
    path('customer', views.customer_list, name='customer_list'),
    path('customer/<int:id>/<slug:slug>/', views.customer_detail, name='customer_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/detail/', views.order_detail, name='order_detail'),
    path('order/detail/<int:order_id>', views.order_product, name='order_product'),
    path('order/list/<int:order_id>', views.order_list_product, name='order_list_product'),
    path('orders/update/<int:order_id>/', views.order_update, name='order_update'),
    path('customers', views.customers, name='customers'),
    path('customers/detail/<int:id>', views.cust_detail, name='cust_detail'),
    path('profile', views.profile, name='profile'),
    path('profile/edit/<int:id>', views.profile_edit, name='profile_edit'),
    
]

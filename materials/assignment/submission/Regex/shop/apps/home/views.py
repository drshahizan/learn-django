# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, OrderItem, Order
from .forms import ProductCreateForm, CategoryCreateForm, CartAddProductForm, OrderCreateForm, OrderStatusForm, EditProfileForm
from django.views.decorators.http import require_POST
from .cart import Cart
from django.contrib.auth.models import User
import matplotlib.pyplot as plt
import numpy as np
from django.db.models import Sum, Count, F
import matplotlib
matplotlib.use('Agg')
import io
import urllib, base64


def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'home/home.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

@login_required(login_url="/login/")
def index(request):
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_sales = sum(order.get_total_cost() for order in Order.objects.filter(paid=True))

    # Aggregate the orders by date and calculate the total sales for each day
    sales_data = Order.objects \
    .filter(paid=True) \
    .values('created__date') \
    .annotate(total_sales=Sum(F('items__price') * F('items__quantity'))) \
    .order_by('created__date')

    # Extract the dates and sales totals into separate lists
    dates = [d['created__date'].strftime('%Y-%m-%d') for d in sales_data]
    sales_totals = [d['total_sales'] for d in sales_data]

    # Plot the data as a line chart using Matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(dates, sales_totals, linewidth=2, marker='o', markersize=5, color='blue')
    ax.set_xlabel('Date', fontsize=14, color='white')
    ax.set_ylabel('Total Sales', fontsize=14, color='white')
    ax.tick_params(axis='both', which='major', labelsize=12, colors='white')
    ax.grid(True)
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')

    # Save the Matplotlib plot to a PNG image buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300)
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the PNG image buffer as base64 and create a data URI string
    sales_chart = urllib.parse.quote(base64.b64encode(image_png))

    # Aggregate the orders by date and count the number of orders for each day
    orders_data = Order.objects \
        .filter(paid=True) \
        .values('created__date') \
        .annotate(total_orders=Count('id')) \
        .order_by('created__date')
    
    # Extract the dates and orders totals into separate lists
    dates = [d['created__date'].strftime('%Y-%m-%d') for d in sales_data]
    orders_totals = [d['total_orders'] for d in orders_data]

    # Plot the data as a line chart using Matplotlib
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.bar(dates, orders_totals, color='blue', width=0.1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Orders')
    ax.tick_params(axis='both')

    # Save the Matplotlib plot to a PNG image buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300)
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the PNG image buffer as base64 and create a data URI string
    orders_chart = urllib.parse.quote(base64.b64encode(image_png))
    
    context = {
        'segment': 'index',
        'total_orders': total_orders,
        'total_products': total_products,
        'total_categories': total_categories,
        'total_sales': total_sales,
        'sales_chart': sales_chart,
        'orders_chart': orders_chart,
    }

    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def product_list(request, category_slug=None):
    segment = 'product_list'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'home/product.html',
                  {'category': category,
                   'categories': categories,
                   'products': products, 'segment': segment})

@login_required(login_url="/login/")
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'home/detail.html',
                  {'product': product})

@login_required(login_url="/login/")
def product_create(request):
    segment = 'product_create'
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            
            return redirect('shop:product_list')
    else:
        form = ProductCreateForm()
    return render(request,
                  'home/product_create.html',
                  {'form': form, 'segment': segment})

@login_required(login_url="/login/")
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method != 'POST':
        return render(request,
                    'home/product_delete.html',
                    {'product': product})
    product.delete()
    return redirect('shop:product_list')
 
@login_required(login_url="/login/")
def product_update(request, product_id):  
    product = get_object_or_404(Product, id=product_id)
    form = ProductCreateForm(instance = product) 
    if request.method != 'POST':
        return render(request,
                    'home/product_update.html',
                    {'product': product, 'form': form})
    else:
        form = ProductCreateForm(request.POST, request.FILES, instance = product) 
        if form.is_valid():  
            form.save()  
            return redirect("shop:product_list")  

@login_required(login_url="/login/")
def category_list(request):
    segment = 'category_list'
    categories = Category.objects.all()
    return render(request,
                  'home/category_list.html',
                  {'categories': categories,'segment': segment})

@login_required(login_url="/login/")
def category_create(request):
    segment = 'category_create'
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            product = form.save()  
            return redirect('shop:category_list')
    else:
        form = CategoryCreateForm()
    return render(request,
                  'home/category_create.html',
                  {'form': form, 'segment': segment})

@login_required(login_url="/login/")
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method != 'POST':
        return render(request,
                    'home/category_delete.html',
                    {'category': category})
    category.delete()
    return redirect('shop:category_list')

@login_required(login_url="/login/")
def category_update(request, category_id):  
    category = get_object_or_404(Category, id=category_id)
    form = CategoryCreateForm(instance = category) 
    if request.method != 'POST':
        return render(request,
                    'home/category_update.html',
                    {'category': category, 'form': form})
    else:
        form = CategoryCreateForm(request.POST, request.FILES, instance = category) 
        if form.is_valid():  
            form.save()  
            return redirect("shop:category_list")  

@login_required(login_url="/login/")    
def customer_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'home/customer_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

@login_required(login_url="/login/")
def customer_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'home/customer_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

@require_POST
@login_required(login_url="/login/")
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('shop:cart_detail')


@require_POST
@login_required(login_url="/login/")
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')

@login_required(login_url="/login/")
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'home/cart_detail.html', {'cart': cart})

@login_required(login_url="/login/")
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.email = request.user.email
            order.customer = request.user  # The logged-in user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,
                          'home/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'home/order_create.html',
                  {'cart': cart, 'form': form})

@login_required(login_url="/login/")
def order_detail(request):
    user_id = request.user.id
    order = Order.get_orders_by_customer(user_id)
    return render(request, 'home/order_summary.html', {'orders': order})

@login_required(login_url="/login/")
def order_product(request, order_id):
    order = get_object_or_404(Order,
                                id=order_id)

    return render(request,
                  'home/order_product.html',
                  {'order': order})

def search(request):
    if request.method == 'POST':
       data = request.POST['search']
       product = Product.objects.filter(name__icontains=data)
       return render(request, 'home/home.html', {'products': product})
    product = Product.objects.all()
    return render(request, 'home/home.html', {'products': product})

def search_customer(request):
    if request.method == 'POST':
       data = request.POST['search']
       product = Product.objects.filter(name__icontains=data)
       return render(request, 'home/customer_list.html', {'products': product})
    product = Product.objects.all()
    return render(request, 'home/customer_list.html', {'products': product})

def search_category(request):
    if request.method == 'POST':
       data = request.POST['search']
       category = Category.objects.filter(name__icontains=data)
       return render(request, 'home/category_list.html', {'categories': category})
    category = Category.objects.all()
    return render(request, 'home/category_list.html', {'categories': category})

def search_product(request):
    if request.method == 'POST':
       data = request.POST['search']
       product = Product.objects.filter(name__icontains=data)
       return render(request, 'home/product.html', {'products': product})
    product = Product.objects.all()
    return render(request, 'home/product.html', {'products': product})

@login_required(login_url="/login/")
def search_order(request):
    if request.method == 'POST':
       data = request.POST['search']
       order = Order.objects.filter(id__icontains=data)
       return render(request, 'home/order_list.html', {'orders': order})
    order = Order.objects.all()
    return render(request, 'home/product.html', {'orders': order})

@login_required(login_url="/login/")
def order_list(request):
    segment = 'order'
    orders = Order.objects.all()
    context = {
        'orders': orders,
        'segment':segment
    }
    return render(request, 'home/order_list.html', context)

@login_required(login_url="/login/")
def order_list_product(request, order_id):
    order = get_object_or_404(Order,
                                id=order_id)

    return render(request,
                  'home/order_list_product.html',
                  {'order': order})

def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = OrderStatusForm(instance=order)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('shop:order_list')
    return render(request, 'home/order_update.html', {'order': order, 'form': form})

@login_required(login_url="/login/")
def customers(request):
    
    orders = Order.objects.all().order_by('-created')
    unique_list = []
    list = []

    for x in orders:
        if x.email not in list:
            unique_list.append(x)
            list.append(x.email)

    context = {
        'customers': unique_list,}
    
    return render(request, 'home/customers.html', context)

@login_required(login_url="/login/")
def cust_detail(request, id):
    order = get_object_or_404(Order, id=id)

    return render(request, 'home/cust_detail.html', {'cust': order})

@login_required(login_url="/login/")
def profile(request):
    
    user = User.objects.filter(id=request.user.id)
    context = {
        'user': user,}
    
    return render(request, 'home/profile.html', context)

@login_required(login_url="/login/")
def profile_edit(request, id):
    user = get_object_or_404(User, id=id)
    form = EditProfileForm(instance = user) 
    if request.method != 'POST':
        return render(request,
                    'home/profile_edit.html',
                    {'user': user, 'form': form})
    else:
        form = EditProfileForm(request.POST, request.FILES, instance = user) 
        if form.is_valid():  
            form.save()  
            return redirect("shop:profile")
    
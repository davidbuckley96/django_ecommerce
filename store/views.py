from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem, Category, User, ShippingAddress
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http.response import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from random import sample

# teste template CSS
# teste template CSS
# teste template CSS
def teste(request):
    return render(request, 'test-home.html')
def teste2(request):
    return render(request, 'test-category.html')
def teste3(request):
    return render(request, 'test-product.html')
def teste4(request):
    return render(request, 'test-login.html')
def teste5(request):
    return render(request, 'test-register.html')
def teste6(request):
    return render(request, 'test-cart-empty.html')
# teste template CSS
# teste template CSS
# teste template CSS


def home(request):
    # recent_products_1 = Product.objects.all().order_by('-date_modified')[:4]
    # recent_products_2 = Product.objects.all().order_by('-date_modified')[4:8]
    # recent_products_3 = Product.objects.all().order_by('-date_modified')[8:12]
    recent_products = Product.objects.all
    sales_products = Product.objects.filter(discount=True).order_by('-date_modified')[:18]
    categories = Category.objects.all()
    digital_products = Product.objects.filter(digital=True)
    random_products = list(Product.objects.all())
    best_sellers = sample(random_products, 8)

    if request.GET.get('q') is not None:
        q = request.GET.get('q')
        page = 'search'
    else:
        q = ''
        page = 'homepage'

    products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(category__name__icontains=q) |
        Q(description__icontains=q)
    ).order_by('name')
    products_count = products.count()

    context = {'recent_products': recent_products, 'categories': categories, 'sales_products': sales_products,
            'products_count': products_count, 'products': products, 'page': page,
            'digital_products': digital_products, 'best_sellers': best_sellers}
    return render(request, 'home.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    delivery_time = (datetime.now() + timedelta(days=4)).date
    description_lines = product.description.split('\n')
    reviews = product.review_set.all()
    reviews_length = len(reviews)

    related_products = Product.objects.filter(category=product.category).order_by('-date_modified')[:5]
    customer_bought = Product.objects.all().order_by('-discount_percent')[:5]
  
    context = {'product': product, 'delivery_time': delivery_time, 'description_lines': description_lines, 'reviews': reviews, 'reviews_length': reviews_length, 'related_products': related_products, 'customer_bought': customer_bought}
    return render(request, 'product.html', context)


def category(request, pk):
    category = Category.objects.get(name=pk)
    products = Product.objects.filter(category=category).order_by('-date_modified')
    products_count = products.count()
    
    context = {'category': category, 'products': products, 'products_count': products_count}
    return render(request, 'category.html', context)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Please enter a valid email and make sure both passwords match')

    context = {'form': form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    items = order.orderitem_set.all()
    context = {'order': order, 'items': items}
    return render(request, 'cart.html', context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    order_items_count = order.orderitem_set.count()
    total_cart_quantity = order.get_cart_quantity
    order_item_quantity = order_item.quantity

    response_data = {
        'message': 'Item was added successfully',
        'order_items_count': order_items_count,
        'total_cart_quantity': total_cart_quantity,
        'order_item_quantity': order_item_quantity,
        'order_item_price': order_item.get_total_value,
        'product_id': product.id,
        'cart_total_price': order.get_cart_total,
    }

    return JsonResponse(response_data, safe=False)


def checkout(request):
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    items = order.orderitem_set.all()
    context = {'order': order, 'items': items}
    return render(request, 'checkout.html', context)

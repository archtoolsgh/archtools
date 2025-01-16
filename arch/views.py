import random
import string
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import *
from .utils import cookieCart, cartData


# Create your views here.
def index(request):
    return render(request, 'index.html')


def architecture(request):
    data = cartData(request)
    cartItems = data['cartItems']
    goods = Products.objects.all()
    type = Type.objects.all()
    products = []
    packages = []
    for p in goods:
        if p.type == type[0]:
            products.append(p)
        else:
            packages.append(p)
    context= {"products": products, "packages":packages, 'cartItems': cartItems,}
    return render(request, 'architecture.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    randomNum = generate_random_string(15)

    context = {'items':items, 'order': order, 'cartItems' : cartItems, 'randomNum': randomNum}
    return render(request, "checkout.html", context)


def engineering(request):
    return render(request, 'engineering.html')


def health(request):
    return render(request, 'health.html')


def products(request):
    return render(request, 'products.html')


def about(request):
    return render(request, 'about.html')

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, "cart.html", context)

def singleProduct(request, product_id):
    products = get_object_or_404(Products, pk=product_id)
    if products.description:
        list = (products.description).split(";")
        context = {"products": products, "list": list}
    else:
        context = {"products": products}
    return render(request, 'singleProduct.html', context)

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def generate_random_string(length):
    # Define the pool of characters (letters and digits)
    characters = string.ascii_letters + string.digits
    # Use random.choices to select random characters from the pool
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

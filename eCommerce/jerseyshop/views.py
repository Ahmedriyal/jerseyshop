from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from .forms import OrderItemForm
import datetime


# Create your views here.

# /----- Views for signup -----/
def register(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems= order['get_cart_items']


    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exist")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already used")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                auth.login(request, user)

                messages.info(request, "User successfully created")
                return redirect('register')
        else:
            messages.error(request, "Password not matching")
            return redirect('register')
    else:
        return render(request, 'html/register.html', {'cartItems': cartItems})


# /----- Views for Signin -----/
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Wrong username or password")
            # return redirect('login')
            # return HttpResponseRedirect('/')
    else:
        return render(request, 'html/login.html')


# /----- Views for Logout -----/
def logout(request):
    auth.logout(request)
    return redirect('/')


# /----- Views for Homepage -----/
def home(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems= order['get_cart_items']

    club_jersey = ClubJerseyDetails.objects.all().order_by('-added_time')[:4]
    national_jersey = NTJerseyDetails.objects.all().order_by('-added_time')[:4]

    context = {'club_jersey': club_jersey, 'national_jersey': national_jersey, 'cartItems': cartItems}
    return render(request, 'html/home.html', context)


# /----- Views for Club jersey page -----/
def club(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems= order['get_cart_items']

    club_jersey = ClubJerseyDetails.objects.all().order_by('-added_time')
    paginator = Paginator(club_jersey, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'cartItems': cartItems}
    return render(request, 'html/club.html', context)


# /----- Views for National jersey page -----/
def country(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems= order['get_cart_items']

    national_jersey = NTJerseyDetails.objects.all().order_by('-added_time')
    paginator = Paginator(national_jersey, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'cartItems': cartItems}
    return render(request, 'html/country.html', context)


# /----- Views for Search -----/
def search_results(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems= order['get_cart_items']

    if request.method == "GET":
        searched = request.GET.get('searched')
        page_obj = ClubJerseyDetails.objects.all().filter(title__icontains=searched)
        page_obj1 = NTJerseyDetails.objects.all().filter(title__icontains=searched)

        return render(request, 'html/search_results.html',
                      {'searched': searched, 'page_obj': page_obj, 'page_obj1': page_obj1, 'cartItems': cartItems})
    else:
        return render(request, 'html/search_results.html', {'cartItems': cartItems})


# /----- Views for National jersey details page -----/
def national_jersey_details(request, national_jersey_id):
    national_jersey = NTJerseyDetails.objects.get(pk=national_jersey_id)

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        order.save()
        cartItems = order.get_cart_items

        if request.method == 'POST':
            form = OrderItemForm(request.POST, request.FILES)
            if form.is_valid():
                orderitem = form.save(commit=False)
                orderitem.national_jersey = national_jersey
                orderitem.order_id = order.id
                orderitem.save()

                return redirect('cart')
        else:
            form = OrderItemForm()

    context = {'form': form, 'national_jersey': national_jersey, 'cartItems': cartItems}
    return render(request, 'html/national_jersey_details.html', context)


# /----- Views for Club jersey details page -----/
def club_jersey_details(request, club_jersey_id):
    club_jersey = ClubJerseyDetails.objects.get(pk=club_jersey_id)

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        order.save()
        cartItems = order.get_cart_items

        if request.method == 'POST':
            form = OrderItemForm(request.POST, request.FILES)
            if form.is_valid():
                orderitem = form.save(commit=False)
                orderitem.club_jersey = club_jersey
                orderitem.order_id = order.id
                orderitem.save()


                # return redirect('cart')
        else:
            form = OrderItemForm()

    context = {'form': form, 'club_jersey': club_jersey, 'cartItems': cartItems}
    return render(request, 'html/club_jersey_details.html', context)


# /----- Views for Cart page -----/
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'html/cart.html', context)


# /----- Views for Remove Item from Cart page -----/
def delete(request, id):
    item = OrderItem.objects.get(id=id)
    item.delete()


    return redirect('cart')


# /----- Views for Checkout page -----/
def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()

        # if request.method == 'POST':
        #     name = request.POST['name']
        #     email = request.POST['email']
        #     mobileNo = request.POST['mobileNo']
        #     address = request.POST['address']
        #
        #     checkout = ShippingInfo(name=name, email=email, mobileNo=mobileNo, address=address)
        #     checkout.order_id = order.id
        #     checkout.user_id = user.id
        #     checkout.save()


    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'html/checkout.html', context)


# def updateItem(request):
#     data = json.loads(request.body)
#     jerseyId = data['jerseyId']
#     action = data['action']
#
#     print('action:', action)
#     print('jerseyId:', jerseyId)
#
#     customer = request.user.customer
#     national_jersey = NTJerseyDetails.objects.get(id=jerseyId)
#     order, created = Order.objects.get_or_create(customer=customer)
#     orderItem, created = OrderItem.objects.create(order=order, national_jersey=national_jersey)
#     orderItem.save()
#
#     return JsonResponse('Item is added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        ShippingInfo.objects.create(user=user, order=order, name=data['form']['name'], email=data['form']['email'],
                                    address=data['form']['address'], mobileNo=data['form']['mobileNo'])
    else:
        print('User is not logged in')

    return JsonResponse('Payment complete', safe=False)



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username']=user.id
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    if 'username' not in request.session:
        return redirect('login')
    uname=request.session['username']
    items = item.objects.all()
    carti = Cart.objects.filter(user=uname).count()
    context = {'its': items,'ca':carti,'uu':uname}
    return render(request, 'home.html', context)

    
def cart_add(request, id):
    cart = Cart(request)
    uname=request.session['username']
    product = item.objects.get(id=id)
    us=User.objects.get(id=uname)
    product = item.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(user=us, item=product,quantity=1)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("home")

def cart(request):
    if 'username' not in request.session:
        return redirect('login')
    user=request.session['username']
    cart_items = Cart.objects.filter(user=user)
    print(cart_items)
    
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)

def remove_from_cart(request, cart_id):
    Cart.objects.filter(id=cart_id).delete()
    return redirect('cart')

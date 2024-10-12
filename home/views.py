from django.shortcuts import render,redirect
from .models import Product,Category,User
from adminpanel.forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'home/index.html',{'products':products})

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Registered')
            return redirect('site_home')
    else:
        form = RegistrationForm()
    return render(request,'home/register.html',{'form':form})

def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('admin_home')
            else:
                messages.error(request,'Invalid Username or Password!!')
                return redirect('sign_in')
    
    else:
        form = LoginForm()
    return render(request,'home/login.html',{'form':form})

def error_page(request):
    return render(request,'home/404.html')
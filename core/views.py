from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from .models import *
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned data is a dictionary
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, you're account is created!")
            return redirect('login_pg')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_pg(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if not username or not password:
                messages.error(request, 'Both username and password are required.')
                return redirect('login_pg')
            user = authenticate(request,username=username,password=password)
            if user is None:
                messages.error(request,'Invalid user or password ')
                return redirect('login_pg')
            else:
                login(request,user)
                return redirect('home') 
    else:
        form = LoginForm()
    return render(request,'login.html',{'form': form})   

def logout_pg(request):
    logout(request)
    return redirect(reverse('login_pg'))
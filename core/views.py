from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
# Create your views here.
def register(request):
    context={}
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login_pg')
    else:
        form = UserRegistrationForm()
    context['form']=form
    return render(request,'register.html',context)

def login_pg(request):
    context={}
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is None:
                messages.error(request,'Invalid password ')
                return redirect('/login/')
            else:
                login(request,user)
                return redirect('home/') 
    else:
        form = LoginForm()
    context['form']=form
    return render(request,'login.html',context)      
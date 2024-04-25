from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages
from webrecipe.forms import *

# Create your views here.
def home(request):
    queryset=Product.objects.all()
    context={'ri':queryset}
    return render(request,'home.html',context)

def create(request):
    submitted=False
    if request.method == 'POST':
        form =CreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request, 'Recipe created successfully.')
            return redirect('/home')
    else:
        form = CreateForm()
    if 'submitted' in request.GET:
        submitted=True
    return render(request,'create.html',{'form':form,'submitted':submitted})

def view(request,id):
    queryset=Product.objects.get(id=id)
    context={'ri':queryset}
    return render(request,'view.html',context)

def edit(request,id):
    queryset = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form =CreateForm(request.POST,request.FILES,instance=queryset)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect('/home/')
            
        queryset.save()
    else:
        form=CreateForm(instance=queryset)
    context = {'form':form,'recipes': queryset}
    return render(request,"create.html",context)

def delete(request,id):
    queryset = Product.objects.get(id=id)
    queryset.delete()    
    return redirect('/home/')
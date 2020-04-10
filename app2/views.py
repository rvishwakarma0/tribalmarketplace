from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,View
from .models import Product
from .forms import Myform,LocalCentreForm,LocalCentreInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from decimal import *


class IndexView(ListView):
    template_name="app2/index.html"

    def get_queryset(self):
        return Product.objects.all()


class Details(DetailView):
    model=Product
    template_name = "app2/detail.html"


class RegisterView(View):
    def get(self,request):
        form=Myform()
        return render(request,"app2/registerproduct.html",{'form':form})

    def post(self,request):
        form=Myform()
        if request.method=='POST':
            form=Myform(request.POST)
            if form.is_valid():
                form.save()
                form=form.save(commit=False)
                if 'image' in request.FILES:
                    form.image=request.FILES['image']
                form.save()
                return redirect('/seller/')
        else:
            form=Myform()
        return render(request,'app2/registerproduct.html',{'form':form})

def productmani(request, id):
    prod = Product.objects.get(id=id)
    if request.method == 'POST':
        ntitle = request.POST.get('ntitle')
        nslug = request.POST.get('nslug')
        ndescription = request.POST.get('ndescription')
        nprice = request.POST.get('nprice')
        prod.title = ntitle
        prod.slug = nslug
        prod.description = ndescription
        prod.price = Decimal(nprice)
        prod.save()
        return redirect('/seller/')
    else:

        return render(request,'app2/productmani.html',{'product':prod})



def productslist(request):
    product_list = Product.objects.all()
    return render(request,'app2/productlist.html',{'products':product_list})

def registerseller(request):
    registered = False
    if request.method == 'POST':
        mform = LocalCentreForm(data=request.POST)
        miform = LocalCentreInfoForm(data=request.POST)
        if mform.is_valid() and miform.is_valid():
            user=mform.save()
            user.set_password(user.password)
            user.save()
            profile = miform.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print("found it")
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True
            return redirect('/seller/')

    else:
        mform = LocalCentreForm()
        miform = LocalCentreInfoForm()
    return render(request,'app2/register.html',{'user_form':mform,'profile_form':miform,'registered':registered})


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/seller/')
            else:
                return HttpResponse("YOur account was inactive.")
        else:
            return HttpResponse("Invalid login detail given")
    else:
        return render(request,'app2/login.html',{})


@login_required
def userlogout(request):
    logout(request)
    return redirect('/seller/')


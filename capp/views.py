from django.shortcuts import render
from app2.models import Product
# Create your views here.
def index(request):
    obj = Product.objects.all()
    return render(request,'capp/index.html',{'object_list':obj})

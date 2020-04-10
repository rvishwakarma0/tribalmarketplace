from django import forms
from app2.models import Product,LocalCentre
from django.contrib.auth.models import User

class Myform(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

class LocalCentreForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')


class LocalCentreInfoForm(forms.ModelForm):
    class Meta:
        model = LocalCentre
        fields = ('profile_pic','pincode','address','city')
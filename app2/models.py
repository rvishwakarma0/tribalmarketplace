from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(blank=True,unique=True)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=20,default=99.99)
    image=models.ImageField(upload_to='product_image',null=True,blank=True)
    featured=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    is_digital=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("capp:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("capp:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("capp:remove-from-cart", kwargs={
            'slug': self.slug
        })



class LocalCentre(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank='True')
    pincode = models.CharField(max_length = 10)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 30)

    def _str_(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code
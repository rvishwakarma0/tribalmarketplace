from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='app2'

urlpatterns= [  path('',views.IndexView.as_view(),name='index'),
                path('register/',views.RegisterView.as_view(),name='register'),
                path('productmani/<int:id>/',views.productmani,name='productmani'),
                path('productslist/',views.productslist,name='productslist'),
                path('registerseller/', views.registerseller, name='register'),
                path('login/', views.userlogin, name='login'),
                path('logout/', views.userlogout, name='logout')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


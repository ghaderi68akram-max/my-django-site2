from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('shop/', views.shop, name='shop'),
]
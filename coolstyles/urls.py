"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('home',views.HomeView.as_view(), name='home'),
    path('update-order',views.CheckoutOrder.as_view(), name='update-order'),
    path('add-item', views.AddItemToOrder.as_view(), name='add-item'),
    path('sendorder', views.SendOrder.as_view(), name='send-order'),
    path('success-pay', views.SuccessRedirect.as_view(), name='success-pay'),
    path('about us', views.About_us.as_view(), name='about-us'),
    path('cart', views.OrderView.as_view(), name='cart'),
    path('checkout', views.Checkout.as_view(), name='checkout')
]

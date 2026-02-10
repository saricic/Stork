"""
URL configuration for stork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('driver/',driver, name='driver' ),
    path('login/',loginPage, name='login'),
    path('register/',register, name='register' ),
    path('reservation/',reservation, name='reservation' ),
    path('orders/',order_list, name='order_list'),
    path('orders/create',create_order, name='create_order'),
    path('orders/delete/<int:pk>/',order_delete, name='order_delete'),
]

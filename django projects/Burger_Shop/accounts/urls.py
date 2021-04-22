from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('regform', views.regform, name="regform"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
    path('user.html', views.user, name="user"),
    path('user_management.html', views.user_management, name="user_management"),
    path('food_management.html', views.food_management, name="food_management"),
    path('order_management.html', views.order_management, name="order_management"),
]

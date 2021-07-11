from django.urls import path
from .import views

urlpatterns = [
    path("shopper", views.shopper, name= 'shopper'),
    path("shopperRegis", views.shopperRegistrations, name= 'shopperRegistrations'),
    path("login", views.login, name= 'login'),
    path("logout", views.logout, name= 'logout'),
]

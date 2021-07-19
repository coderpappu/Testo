from django.urls import path
from .import views

urlpatterns = [
    path("shopper", views.shopper, name= 'shopper'),
    path("shopperRegis", views.shopperRegistrations, name= 'shopperRegistrations'),
    path("userORseller", views.userAndSeller, name= 'userAndSeller'),
    path("login", views.loginUser, name= 'login'),
    path("logout", views.logout, name= 'logout'),
]

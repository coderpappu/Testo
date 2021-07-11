from django.urls import path
from .import views

urlpatterns = [
    path("", views.shopperProductsShow, name= 'shopperProductsShow'),
    path("delete/<int:id>", views.productDelete, name= 'productDelete'),
    path("deleteTop/<int:id>", views.deleteTop, name= 'deleteTop'),
    path("update/<int:id>", views.productUpdate, name= 'productUpdate'),
    path("topProducts/<int:id>", views.topProduct, name= 'topProduct'),
    path("shopEvent", views.shop_Event, name= 'shop_Event'),
    path("shopEventDelet/<int:id>", views.deleteEvent, name= 'deleteEvent'),
    # path("shopAdmin/", views.topProductShow, name= 'topProductShow'),
]

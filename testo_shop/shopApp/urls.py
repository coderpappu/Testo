from django.urls import path
from .import views

urlpatterns = [
    path("", views.proDuctView, name= 'proDuctView'),
    # path("topProductShow/", views.topProductPublish, name= 'topProductPublish'),
]

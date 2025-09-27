from django.urls import path
from . import views

urlpatterns = [
    path("", views.purchase_list, name="purchase_list"),
    path("new/", views.purchase_create, name="purchase_create"),
]
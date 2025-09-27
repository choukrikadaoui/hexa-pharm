from django.urls import path
from . import views

urlpatterns = [
    path("", views.supplier_list, name="supplier_list"),
    path("new/", views.supplier_create, name="supplier_create"),
]
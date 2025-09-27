from django.urls import path
from . import views

urlpatterns = [
    path("", views.medicine_list, name="medicine_list"),
    path("new/", views.medicine_create, name="medicine_create"),
    path("<int:pk>/edit/", views.medicine_update, name="medicine_update"),
]
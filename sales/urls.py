from django.urls import path
from . import views

urlpatterns = [
    path("", views.sale_list, name="sale_list"),
    path("pos/", views.pos_screen, name="pos_screen"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.sale_list, name="sale_list"),
    path("pos/", views.pos_screen, name="pos_screen"),
    path("<int:pk>/", views.sale_detail, name="sale_detail"),
    path("<int:pk>/edit/", views.sale_update, name="sale_update"),
    path("<int:pk>/delete/", views.sale_delete, name="sale_delete"),
]
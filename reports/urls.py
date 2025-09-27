from django.urls import path
from . import views

urlpatterns = [
    path("low-stock/", views.low_stock, name="low_stock"),
    path("near-expiry/", views.near_expiry, name="near_expiry"),
]
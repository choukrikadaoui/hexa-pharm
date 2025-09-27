from django.contrib import admin
from .models import Customer, Sale, SaleItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    search_fields = ("name", "phone")

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "date", "total_incl_tax")
    list_filter = ("date",)

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ("sale", "medicine", "quantity", "unit_price")
    list_filter = ("sale__date",)
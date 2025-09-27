from django.contrib import admin
from .models import Purchase, PurchaseItem

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("id", "supplier", "invoice_no", "date")
    list_filter = ("date", "supplier")

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ("purchase", "medicine", "lot_no", "quantity", "purchase_price")
    list_filter = ("expiry_date",)
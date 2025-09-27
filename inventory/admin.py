from django.contrib import admin
from .models import Medicine, Batch, StockMove

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "barcode", "form", "strength", "unit_price", "min_stock", "is_active")
    search_fields = ("name", "barcode")

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("medicine", "lot_no", "expiry_date", "quantity_on_hand", "sell_price")
    list_filter = ("expiry_date",)

@admin.register(StockMove)
class StockMoveAdmin(admin.ModelAdmin):
    list_display = ("batch", "move_type", "quantity", "ref", "created_at")
    list_filter = ("move_type", "created_at")
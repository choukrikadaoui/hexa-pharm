from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=64, blank=True, null=True, unique=True)
    atc_code = models.CharField(max_length=32, blank=True, null=True)
    form = models.CharField(max_length=64, blank=True, null=True)   # comprimé, sirop...
    strength = models.CharField(max_length=64, blank=True, null=True) # 500mg
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # %
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    min_stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Batch(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name="batches")
    lot_no = models.CharField(max_length=64)
    expiry_date = models.DateField()
    quantity_on_hand = models.IntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("medicine", "lot_no")
        ordering = ["expiry_date"]

    def __str__(self):
        return f"{self.medicine.name} | Lot {self.lot_no} | EXP {self.expiry_date}"

class StockMove(models.Model):
    IN = "IN"; OUT = "OUT"
    MOVE_TYPES = [(IN, "IN"), (OUT, "OUT")]
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="moves")
    move_type = models.CharField(max_length=3, choices=MOVE_TYPES)
    quantity = models.IntegerField()
    ref = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
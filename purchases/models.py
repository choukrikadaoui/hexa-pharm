from django.db import models, transaction
from suppliers.models import Supplier
from inventory.models import Medicine, Batch, StockMove
from django.utils import timezone

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    invoice_no = models.CharField(max_length=64, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"PO #{self.id} - {self.supplier}"

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    lot_no = models.CharField(max_length=64)
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.medicine} x{self.quantity}"

    def receive(self):
        # Create or update batch, then stock move IN
        batch, _ = Batch.objects.get_or_create(
            medicine=self.medicine,
            lot_no=self.lot_no,
            defaults={
                "expiry_date": self.expiry_date,
                "quantity_on_hand": 0,
                "purchase_price": self.purchase_price,
                "sell_price": self.sell_price,
            },
        )
        # Update batch meta if changed
        batch.expiry_date = self.expiry_date
        batch.purchase_price = self.purchase_price
        batch.sell_price = self.sell_price
        batch.quantity_on_hand += self.quantity
        batch.save()
        StockMove.objects.create(batch=batch, move_type=StockMove.IN, quantity=self.quantity, ref=f"PO#{self.purchase_id}")

    @transaction.atomic
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.receive()
from django.db import models, transaction
from inventory.models import Medicine, Batch, StockMove
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name or "Client comptoir"

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sale #{self.id}"

    @property
    def total_excl_tax(self):
        return sum(item.subtotal_excl_tax for item in self.items.all()) - self.discount

    @property
    def total_tax(self):
        return sum(item.tax_amount for item in self.items.all())

    @property
    def total_incl_tax(self):
        return self.total_excl_tax + self.total_tax

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    @property
    def subtotal_excl_tax(self):
        return self.unit_price * self.quantity

    @property
    def tax_amount(self):
        return self.subtotal_excl_tax * (self.tax_rate / 100)

    def __str__(self):
        return f"{self.medicine} x{self.quantity}"

    def _consume_fifo(self, qty):
        # Consume from earliest-expiring batches first
        remaining = qty
        for batch in Batch.objects.filter(medicine=self.medicine, quantity_on_hand__gt=0).order_by("expiry_date", "id"):
            take = min(remaining, batch.quantity_on_hand)
            if take <= 0:
                continue
            batch.quantity_on_hand -= take
            batch.save()
            StockMove.objects.create(batch=batch, move_type=StockMove.OUT, quantity=take, ref=f"SALE#{self.sale_id}")
            remaining -= take
            if remaining == 0:
                break
        if remaining > 0:
            raise ValueError("Stock insuffisant pour compléter la vente")

    @transaction.atomic
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if self.tax_rate is None:
            self.tax_rate = self.medicine.tax_rate
        if self.unit_price is None:
            self.unit_price = self.medicine.unit_price
        super().save(*args, **kwargs)
        if is_new:
            self._consume_fifo(self.quantity)
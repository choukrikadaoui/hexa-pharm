from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from inventory.models import Medicine, Batch
from django.db.models import Sum

@login_required
def low_stock(request):
    # Medicines with stock below minimum threshold
    low_stock_medicines = []
    for medicine in Medicine.objects.filter(is_active=True):
        total_stock = medicine.batches.aggregate(total=Sum('quantity_on_hand'))['total'] or 0
        if total_stock <= medicine.min_stock:
            low_stock_medicines.append({
                'medicine': medicine,
                'current_stock': total_stock,
                'min_stock': medicine.min_stock
            })

    return render(request, "reports/low_stock.html", {"low_stock_medicines": low_stock_medicines})

@login_required
def near_expiry(request):
    # Batches expiring in the next 30 days
    threshold_date = timezone.now().date() + timedelta(days=30)
    near_expiry_batches = Batch.objects.filter(
        expiry_date__lte=threshold_date,
        quantity_on_hand__gt=0
    ).order_by('expiry_date')

    return render(request, "reports/near_expiry.html", {"near_expiry_batches": near_expiry_batches})
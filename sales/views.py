from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Sale, SaleItem
from .forms import SaleForm, SaleItemForm

@login_required
def sale_list(request):
    return render(request, "sales/sale_list.html", {"sales": Sale.objects.all().order_by("-date")})

@login_required
def pos_screen(request):
    sale_form = SaleForm(request.POST or None)
    item_form = SaleItemForm(request.POST or None)
    if request.method == "POST" and sale_form.is_valid() and item_form.is_valid():
        sale = sale_form.save()
        item = item_form.save(commit=False)
        item.sale = sale
        try:
            item.save()  # triggers FIFO consume
        except Exception as e:
            messages.error(request, str(e))
            sale.delete()
            return redirect("pos_screen")
        messages.success(request, f"Vente #{sale.id} créée. Total TTC: {sale.total_incl_tax}")
        return redirect("sale_list")
    return render(request, "sales/pos.html", {"sale_form": sale_form, "item_form": item_form})

@login_required
def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    items = sale.items.all().select_related('medicine')
    return render(request, "sales/sale_detail.html", {"sale": sale, "items": items})

@login_required
def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            messages.success(request, f"Vente #{sale.id} mise à jour avec succès.")
            return redirect("sale_detail", pk=sale.pk)
    else:
        form = SaleForm(instance=sale)
    return render(request, "sales/sale_update.html", {"form": form, "sale": sale})

@login_required
def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        sale_id = sale.id
        sale.delete()
        messages.success(request, f"Vente #{sale_id} supprimée avec succès.")
        return redirect("sale_list")
    return render(request, "sales/sale_delete.html", {"sale": sale})
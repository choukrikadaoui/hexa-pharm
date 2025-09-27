from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Sale
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
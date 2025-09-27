from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from .models import Purchase, PurchaseItem
from .forms import PurchaseForm, PurchaseItemForm

@login_required
def purchase_list(request):
    return render(request, "purchases/purchase_list.html", {"purchases": Purchase.objects.all().order_by("-date")})

@login_required
def purchase_create(request):
    form = PurchaseForm(request.POST or None)
    item_form = PurchaseItemForm(request.POST or None)
    if request.method == "POST" and form.is_valid() and item_form.is_valid():
        purchase = form.save()
        item = item_form.save(commit=False)
        item.purchase = purchase
        item.save()  # triggers stock IN
        return redirect("purchase_list")
    return render(request, "purchases/purchase_form.html", {"form": form, "item_form": item_form})
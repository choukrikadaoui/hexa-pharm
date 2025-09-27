from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Supplier
from .forms import SupplierForm

@login_required
def supplier_list(request):
    return render(request, "suppliers/supplier_list.html", {"suppliers": Supplier.objects.all()})

@login_required
def supplier_create(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("supplier_list")
    return render(request, "suppliers/supplier_form.html", {"form": form})
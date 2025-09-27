from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Medicine
from .forms import MedicineForm

@login_required
def medicine_list(request):
    q = request.GET.get("q", "")
    meds = Medicine.objects.all()
    if q:
        meds = meds.filter(name__icontains=q)
    return render(request, "inventory/medicine_list.html", {"medicines": meds, "q": q})

@login_required
def medicine_create(request):
    form = MedicineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("medicine_list")
    return render(request, "inventory/medicine_form.html", {"form": form})

@login_required
def medicine_update(request, pk):
    obj = get_object_or_404(Medicine, pk=pk)
    form = MedicineForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("medicine_list")
    return render(request, "inventory/medicine_form.html", {"form": form})
from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["name", "barcode", "form", "strength", "manufacturer", "tax_rate", "unit_price", "min_stock", "is_active"]
        widgets = {f: forms.TextInput(attrs={"class": "form-control"}) for f in ["name", "barcode", "form", "strength", "manufacturer"]}
        widgets.update({
            "tax_rate": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "min_stock": forms.NumberInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        })
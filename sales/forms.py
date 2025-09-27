from django import forms
from .models import Sale, SaleItem

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["customer", "discount", "notes"]
        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "discount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ["medicine", "quantity", "unit_price", "tax_rate"]
        widgets = {
            "medicine": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "tax_rate": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }
from django import forms
from .models import Purchase, PurchaseItem

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["supplier", "invoice_no", "date", "notes"]
        widgets = {
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "invoice_no": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ["medicine", "lot_no", "expiry_date", "quantity", "purchase_price", "sell_price"]
        widgets = {
            "medicine": forms.Select(attrs={"class": "form-control"}),
            "lot_no": forms.TextInput(attrs={"class": "form-control"}),
            "expiry_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "purchase_price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "sell_price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }
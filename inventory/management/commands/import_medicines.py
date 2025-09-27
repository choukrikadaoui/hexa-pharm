from django.core.management.base import BaseCommand
from inventory.models import Medicine
import csv

class Command(BaseCommand):
    help = "Import medicines from CSV with headers: name,barcode,form,strength,manufacturer,tax_rate,unit_price,min_stock"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs["csv_file"], encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                Medicine.objects.update_or_create(
                    barcode=r.get("barcode") or None,
                    defaults={
                        "name": r["name"],
                        "form": r.get("form"),
                        "strength": r.get("strength"),
                        "manufacturer": r.get("manufacturer"),
                        "tax_rate": r.get("tax_rate") or 0,
                        "unit_price": r.get("unit_price") or 0,
                        "min_stock": r.get("min_stock") or 0,
                    },
                )
        self.stdout.write(self.style.SUCCESS("✅ Import terminé"))
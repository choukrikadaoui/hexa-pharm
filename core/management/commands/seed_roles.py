from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Create default roles/groups"

    def handle(self, *args, **kwargs):
        roles = ["Admin", "Pharmacist", "Cashier"]
        for name in roles:
            Group.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("Roles created / ensured."))
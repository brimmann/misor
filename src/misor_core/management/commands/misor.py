from django.core.management.base import BaseCommand
from misor_core.main import misor

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Misor is working on your MIS...")
        self.stdout.write(f"current tables: {misor.get_tables()}")
        misor.handle()


from django.core.management.base import BaseCommand
from news.rss import fetch_and_store

class Command(BaseCommand):
    help = "Fetch BZ Basel RSS and store news items."

    def handle(self, *args, **options):
        created, updated = fetch_and_store()
        self.stdout.write(self.style.SUCCESS(f"created={created}, updated={updated}"))

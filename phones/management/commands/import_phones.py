import csv

from django.core.management.base import BaseCommand
from work_with_database1.phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            phone = Phone(
                id=phone_data['id'],
                name=phone_data['name'],
                image=phone_data['image'],
                price=phone_data['price'],
                release_date=phone_data['release_date'],
                lte_exists=phone_data['lte_exists']
            )
            phone.save()
            self.stdout.write(self.style.SUCCESS(f"Phone '{phone.name}' saved successfully."))
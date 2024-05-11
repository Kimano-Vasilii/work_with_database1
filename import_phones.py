import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                _, created = Phone.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    image=row[2],
                    price=row[3],
                    release_date=row[4],
                    lte_exists=row[5]
                )
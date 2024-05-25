import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                try:
                    phone = Phone.objects.get(id=row[0])
                except ObjectDoesNotExist:
                    phone = Phone()

                phone.id = row[0],
                phone.name = row[1],
                phone.image = row[2],
                phone.price = row[3],
                phone.release_date = row[4],
                phone.lte_exists = row[5],
                phone.save()

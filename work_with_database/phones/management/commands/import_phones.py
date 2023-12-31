import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            Phone(id = int(phone['id']),
                  name = phone['name'],
                  price = int(phone['price']), 
                  image = phone['image'],
                  release_date = datetime.strptime(phone['release_date'], '%Y-%m-%d'),
                  lte_exists = phone['lte_exists'],
                  slug = slugify(phone['name'])
                ).save()

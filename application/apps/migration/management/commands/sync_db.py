from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **kwargs):
        query = "SELECT * FROM porn_category"
        with connections["mysql"].cursor() as cursor:
            cursor.execute(query)
            print(cursor.description)
            row = cursor.fetchone()

        print(row)

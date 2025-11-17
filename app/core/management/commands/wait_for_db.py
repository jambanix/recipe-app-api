"""
Django command to wait for the database to become available
"""

from django.core.management import BaseCommand
from django.db.utils import OperationalError
import time
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for the database"""
    
    def handle(self, *args, **kwargs):
        """ Entry point for command """
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable - waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is now available"))
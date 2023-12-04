#django command to wait for db availability

from django.core.management.base import BaseCommand

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management import BaseCommand


class  Command(BaseCommand):
    #command to wait for database
    
    def hand(self,*args,**options):
        self.stdout.write("waiting for db")
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up =True
            except (Psycopg2OpError, OperationalError):
                self.stderr.write('Database unavailable, waiting...')
                time.sleep(1)
            self.stdout.write(self.style.SUCCESS('DATABASE available '))
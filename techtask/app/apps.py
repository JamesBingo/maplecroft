from django.apps import AppConfig

import csv
from itertools import islice

COUNTRY_NAME = 0
COUNTRY_CODE = 1
COUNTRY_LNG = 2
COUNTRY_LAT = 3
HEADER_ROWS = 1

class AppConfig(AppConfig):
    name = 'app'

    # read countries into memory hash table for speed
    # no need for a full blown database for this data size
    def ready(self):
        global countries
        with open('countries.csv') as f:
            reader = csv.reader(f)
            reader = islice(reader,HEADER_ROWS,None)
            countries = dict()
            for row in reader:
                if any(data for data in row):
                    country = row[COUNTRY_NAME].lower().replace(" ", "")
                    countries[country] = ( row[COUNTRY_CODE],
                                           float(row[COUNTRY_LAT]) if not row[COUNTRY_LAT]=='None' else None,
                                           float(row[COUNTRY_LNG]) if not row[COUNTRY_LNG]=='None' else None)


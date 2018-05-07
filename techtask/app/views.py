from django.shortcuts import render
from django.http import HttpResponse

import csv
from itertools import islice
import re
import json

import twitter

from keys import *

COUNTRY_NAME = 0
COUNTRY_CODE = 1
COUNTRY_LNG = 2
COUNTRY_LAT = 3
HEADER_ROWS = 1


# read into memory hash table for speed
with open('countries.csv') as f:
    reader = csv.reader(f)
    reader = islice(reader,HEADER_ROWS,None)
    countries = dict()
    countriesEscaped = list()
    for row in reader:
        if any(data for data in row):
            country = row[COUNTRY_NAME].lower().replace(" ", "")
            countries[country] = ( row[COUNTRY_CODE],
                                   float(row[COUNTRY_LAT]) if not row[COUNTRY_LAT]=='None' else None,
                                   float(row[COUNTRY_LNG]) if not row[COUNTRY_LNG]=='None' else None)
            countriesEscaped.append(re.escape(country))

# build reg-ex
matcher = re.compile('|'.join(countriesEscaped),re.IGNORECASE)

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def index(request):

    # mock data cos twitter wont give me an app key
    #tweets = ['hello france', 'we love #bulgaria', 'united kingdom']

    # 
    tweets = api.GetUserTimeline(screen_name='MaplecroftRisk',exclude_replies=True)

    locations = list()
    for tweet in tweets:
        matches = matcher.findall(tweet.text.replace(" ", ""))
        for country in matches:
            location = { 'text': tweet.text,
                         'lat' : countries[country.lower()][1],
                         'lng' : countries[country.lower()][2] }
            locations.append(location)

    context = {'mapsKey': MAPS_KEY, 'locations': json.dumps(locations), 'tweets': tweets}

    return render(request, 'index.html', context)

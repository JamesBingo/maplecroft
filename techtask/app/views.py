from django.shortcuts import render
from django.http import HttpResponse

import re
import json

import twitter

from keys import *

from app.apps import countries

# build reg-ex
countriesEscaped = list()
for country in countries.keys():
    countriesEscaped.append(re.escape(country))
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

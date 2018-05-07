# Intro

Maplecroft technical task. Display latest X tweets textually and on a map.

Python3 only.

# Install (Linux)

Grab the repo first:

```
git clone https://github.com/JamesBingo/maplecroft.git
```

Installation using virtualenv (recommended), change into the `maplecroft` directory created in the previous step:

```
virtualenv --python=python3 env
```

Activate the enviroment:

```
source env/bin/activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

# Getting Started

## Keys

The app uses both google maps and twitter apis, both require authentication keys. Create a `keys.py` file in the `techtask` directory with the following format

```
# Google Key
MAPS_KEY = ""

# Twitter Keys
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
```

Instructions on how to obtain keys: [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key) | [Twitter](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens)


## Usage

If not already, change into the `techtask` directory:

```
python manage.py runserver
```

Point the browser at http://localhost:8000/home :)

### Google Maps
The application uses google maps as the map plotting engine. Click on a marker to display tweet content. The marker will fan out (spider) if multiple tweets referenced the same country.

### Tweets
The number of tweets can be specfied in the url:

```
http://localhost:8000/home/<count>
```

Note: This is the count provided to the twitter api which peforms filtering after it has got all replies and retweets. Actual number of analysed tweets is shown in brackets in the 'Tweets' column.
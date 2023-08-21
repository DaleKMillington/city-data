# City Data

## Overview
City Data is a project that leverages data from [Open Weather Map](https://openweathermap.org/) to provide forecasts for various metrics
and translates this information into visualisations within a compact web application.

This endeavor is a personal initiative that employs the following technologies:

- Django
- Django-Rest-Framework
- React
- TypeScript
- SASS
- Vite

## Prerequisites
Before you get started, ensure that you have the following software installed:

- Python (with poetry or pip)
- Node.js (with npm)
- Free account at [Open Weather Data](https://home.openweathermap.org/users/sign_up)

## Setup

### Backend
To begin start by installing the Python dependencies and activating a virtual environment.
The project was built with poetry but the requirements.txt is present if you would prefer to use pip.

#### Migrations
Once you have the Python dependencies installed, the next step is to run the Django migrations to create
the SQLLite database in your project.

```bash
python manage.py migrate 
```

#### Django API Key
Next open a django shell and run the following code to produce an API key
(Choose a name of your choice).

```bash
python manage.py shell
```
```python
from backend.models import APIUser
api_user = APIUser.objects.create(name='your name')
print(api_user.api_key)
```
Make a copy of this API key as this will be needed later.

#### Django Environment Variables
The Django application has a single environment variable named `OPEN_WEATHER_MAP_API_KEY`
which is obtainable from (Open Weather Map)[https://home.openweathermap.org/api_keys] after you have made the free account.

#### Create City Data
The next step is to create some city data. You can use Django Admin for this but it is much quicker 
to POST the data using a tool like Postman. 

```
http://localhost:8000/api/v1.0/city/
```

The API key you previously generated using Django shell will need to be added to the request header
under a field called `X-API-KEY`.

You are free to create whatever City data you choose, however here is an example JSON:

```json
[
  {
    "name": "London",
    "latitude": 51.5074,
    "longitude": -0.1278
  },
  {
    "name": "Paris",
    "latitude": 48.8566,
    "longitude": 2.3522
  },
  {
    "name": "Berlin",
    "latitude": 52.5200,
    "longitude": 13.4050
  },
  {
    "name": "Rome",
    "latitude": 41.9028,
    "longitude": 12.4964
  },
  {
    "name": "Madrid",
    "latitude": 40.4168,
    "longitude": -3.7038
  },
  {
    "name": "Lisbon",
    "latitude": 38.7223,
    "longitude": -9.1393
  },
  {
    "name": "Vienna",
    "latitude": 48.2082,
    "longitude": 16.3738
  },
  {
    "name": "Amsterdam",
    "latitude": 52.3676,
    "longitude": 4.9041
  },
  {
    "name": "Brussels",
    "latitude": 50.8503,
    "longitude": 4.3517
  },
  {
    "name": "Stockholm",
    "latitude": 59.3293,
    "longitude": 18.0686
  },
  {
    "name": "Copenhagen",
    "latitude": 55.6761,
    "longitude": 12.5683
  },
  {
    "name": "Oslo",
    "latitude": 59.9139,
    "longitude": 10.7522
  },
  {
    "name": "Dublin",
    "latitude": 53.3498,
    "longitude": -6.2603
  },
  {
    "name": "Helsinki",
    "latitude": 60.1695,
    "longitude": 24.9354
  },
  {
    "name": "Budapest",
    "latitude": 47.4979,
    "longitude": 19.0402
  },
  {
    "name": "Warsaw",
    "latitude": 52.2297,
    "longitude": 21.0122
  },
  {
    "name": "Athens",
    "latitude": 37.9838,
    "longitude": 23.7275
  },
  {
    "name": "Prague",
    "latitude": 50.0755,
    "longitude": 14.4378
  },
  {
    "name": "Bratislava",
    "latitude": 48.1486,
    "longitude": 17.1077
  },
  {
    "name": "Ljubljana",
    "latitude": 46.0569,
    "longitude": 14.5058
  }
]
```

Finally, make a POST request to the following endpoint (with no payload) 
to fetch and build the weather data.

```
http://localhost:8000/backend-build/
```

### Frontend

#### 
To begin navigate into the frontend directory:
```bash
cd frontend
```
And install the npm dependencies:
```bash
npm install
```

#### Vite Environment Variables
There are two environment variables that need to be set for the frontend to work
- VITE_API_BASE_URL: `http://localhost:8000/api/v1.0`
- VITE_X_API_KEY: Your Django API key

After these environment variables are set, run the frontend (ensure the backend is running in a separate terminal):
```bash
npm run dev
```

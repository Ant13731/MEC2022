# pip install -U googlemaps
# pip install python_weather
# pip install meteostat
# pip install -r requirements.txt

import asyncio
import os

# import googlemaps as gmaps
import geopy as geopy
import meteostat as meteostat
import python_weather as pyWeather

# returns latitude/longitude coords and the point in a different format
def get_coords(city = "", province = "", country = ""):
    location = geopy.geocoders.GeoNames(username="lambda_pandas").geocode(city + "," + province + "," + country)
    print("Got coordinates for", location, "\nLatitude:", location.latitude, "\nLongitude", location.longitude)
    return location.latitude, location.longitude, location.point

# def get_hourly(lat, long):


lat, long, _ = get_coords("Hamilton", "Ontario")

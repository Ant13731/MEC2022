# pip install -U googlemaps
# pip install python_weather
# pip install meteostat
# pip install -r requirements.txt

import asyncio
import os

# import googlemaps as gmaps
import geopy as geopy
import meteostat as meteostat
import datetime
import math
import pandas
import time

NUM_OF_SEGMENTS = 3

# returns latitude/longitude coords and the point in a different format
def get_coords(source = ""):
    location = geopy.geocoders.GeoNames(username="lambda_pandas").geocode(source)
    print("Got coordinates for", location, "\nLatitude:", location.latitude, "\nLongitude", location.longitude)
    return location.latitude, location.longitude

# returns all data points from a certain time
def get_hourly(lat, long):
    start = datetime.datetime.now() - datetime.timedelta(1000)
    dataPoint = meteostat.Point(lat, long)
    data = meteostat.Hourly(dataPoint, start, datetime.datetime.now())
    data:pandas.DataFrame = data.fetch()
    return data

def get_distance(source, destination):
    source_lat, source_long= get_coords(source)
    destination_lat, destination_long = get_coords(destination)
    distance = math.sqrt((source_lat - destination_lat)**2 + (source_long - destination_long)**2)
    midpoint_lat = (source_lat + destination_lat) /2
    midpoint_long = (source_long + source_long) /2
    return distance, midpoint_lat, midpoint_long

def get_map_data(source, destination = None):
    if destination == None:
        distance = 10
        mid_lat, mid_long = get_coords(source)
    else:
        distance, mid_lat, mid_long = get_distance(source, destination)
    bottom_left_lat = (mid_lat - distance + 180) % 360 - 180# y
    bottom_left_long = (mid_long - distance + 180) % 360 - 180 # x

    interval_lat = distance * 2 / NUM_OF_SEGMENTS
    # 16:9 aspect ratio - x needs to be longer
    interval_long = distance * 16/9 * 2 /NUM_OF_SEGMENTS

    data = [None]*NUM_OF_SEGMENTS
    i = 0
    # iterate over x values
    while i < NUM_OF_SEGMENTS:
        data[i] = [None]*NUM_OF_SEGMENTS
        j = 0
        #iterate over y values
        while j < NUM_OF_SEGMENTS:
            in_lat, in_long = (bottom_left_lat + j * interval_lat + 180) % 360 - 180, (bottom_left_long + i * interval_long + 180) % 360 - 180
            dataForPoint = get_hourly(in_lat, in_long)
            data[i][j] = dataForPoint
            if dataForPoint.size == 0:
                print("Couldn't retrieve data for", in_lat, ",", in_long)
            j += 1
        i += 1
    return data

COLORS = ['#CBC3E3','#ADD8E6', '#FFFFE0','#FFD580' ,'#FFCCCB']
GREY= '#808080'
ARROW_SIZE = [0,1,2,3,4]

def get_temp_color_map(data):
    temp_min = 60
    temp_max = -40
    for i in range(NUM_OF_SEGMENTS):
        for j in range(NUM_OF_SEGMENTS):
            try:
                dataPointTemp = data[i][j].get("temp").iat[-1]
                if dataPointTemp < temp_min:
                    temp_min = dataPointTemp
                if dataPointTemp > temp_max:
                    temp_max = dataPointTemp
            except:
                a = 0
    temp_interval = (temp_max - temp_min)/(len(COLORS)-1)
    temp_map = [None] * NUM_OF_SEGMENTS
    for i in range(NUM_OF_SEGMENTS):
        temp_map[i] = [None] * NUM_OF_SEGMENTS
        for j in range(NUM_OF_SEGMENTS):
            temp_map[i][j] = COLORS[math.floor((data[i][j].get("temp").iat[-1]-temp_min)/temp_interval)] if data[i][j].get("temp").size > 0 else GREY
    return temp_map
def get_wind_speed_map(data):
    wind_speed_min = 60
    wind_speed_max = -40
    for i in range(NUM_OF_SEGMENTS):
        for j in range(NUM_OF_SEGMENTS):
            try:
                dataPointWindSpeed = data[i][j].get("wspd").iat[-1]
                if dataPointWindSpeed < wind_speed_min:
                    wind_speed_min = dataPointWindSpeed
                if dataPointWindSpeed > wind_speed_max:
                    wind_speed_max = dataPointWindSpeed
            except:
                a = 0
    wind_speed_interval = (wind_speed_max - wind_speed_min)/(len(ARROW_SIZE)-1)

    wind_map = [None] * NUM_OF_SEGMENTS
    for i in range(NUM_OF_SEGMENTS):
        wind_map[i] = [None] * NUM_OF_SEGMENTS
        for j in range(NUM_OF_SEGMENTS):
            #left side of tuple is the size, right size is the direction in degrees
            wind_map[i][j] = (ARROW_SIZE[math.floor((data[i][j].get("wspd").iat[-1]-wind_speed_min)/wind_speed_interval)], data[i][j].get("wdir").iat[-1]) if data[i][j].get("wspd").size > 0 and data[i][j].get("wdir").size > 0 else (None, None)

    return wind_map

print("Test results for Hamilton, Ontario")
print("Colour map:",get_temp_color_map(get_map_data("Hamilton, Ontario")))
print("Wind map:",get_wind_speed_map(get_map_data("Hamilton, Ontario")))

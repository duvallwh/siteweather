"""
This module contains functions to handle the API calls to the Synoptic and WeatherAPIs.
The config module is a config.py file on gitignore that contains the API tokens.
"""

import json
import logging
import pandas as pd
import requests

from .config import SYNOPTICTOKEN, TOKENWAPI

logging.basicConfig(level=logging.INFO)

def find_ground_stations(lat, lon, radius=30, limit=50, token=SYNOPTICTOKEN):
    """Find the closest ground stations to a given lat/lon point."""
    req = f"https://api.synopticdata.com/v2/stations/metadata?token={token}&radius={lat},{lon},{radius}&limit={limit}"
    res = requests.get(req)

    if res.status_code == 200:
        data_dict = json.loads(res.text)
        return data_dict
        
    else:
        logging.debug(f"Error: {res.status_code} - {res.text}")
        return None
    
def get_20_day_forcast(lat, lon, token=TOKENWAPI):
    req = f"https://api.weatherapi.com/v1/forecast.json?key={token}&q={lat},{lon}&days=20&aqi=no&alerts=no"
    res = requests.get(req)
    forcast_dict = json.loads(res.text)

    output_list = []
    for d in forcast_dict['forecast']['forecastday']:
        day_dict = d['day']
        day_dict['date'] = d['date']
        output_list.append(day_dict)

    forcast_data = pd.DataFrame(output_list)
    forcast_data['date'] = pd.to_datetime(forcast_data['date'])

    return forcast_data
    
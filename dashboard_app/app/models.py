from pandas.io.json import json_normalize
import pandas as pd
import requests

class EarthquakeMonth:
    '''Represents the observations gathered
    for all earthquakes on earth over the
    course of a mont.'''
    def __init__(self):
        # earthquake_month_url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
        # self.response = requests.get(earthquake_month_url)
        # self.df = json_normalize(self.response.json()['features'])
        self.df = pd.read_csv('../earthquakes_data_Feb_2016.csv')
        self.max_mag_row = self.df.ix[self.df['properties.mag'].idxmax(),]

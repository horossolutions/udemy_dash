from pandas.io.json import json_normalize
import pandas as pd
import requests
from nvd3 import discreteBarChart
from flask import Markup

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


class DashboardBarWidget:

    def __init__(self, chart_name, height, width,
        xdata, ydata):
        self.chart_name = chart_name
        self.height = height
        self.width = width
        self.xdata = xdata
        self.ydata = ydata

    def get_html(self):
        chart_type = self.chart_name
        chart = discreteBarChart(
            name=chart_type,
            height=self.height,
            width=self.width,
            jquery_on_ready=True)
        chart.add_serie(
            y=self.ydata,
            x=self.xdata)
        chart.buildhtml()
        return Markup(chart.htmlcontent)

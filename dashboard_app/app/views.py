from app import app
from .models import EarthquakeMonth
from flask import render_template


@app.route('/')
def index():
    earthquake_month = EarthquakeMonth()
    max_mag_row = earthquake_month.max_mag_row
    max_mag_place = max_mag_row['properties.place']
    max_mag_mag = max_mag_row['properties.mag']
    context = {
        'max_mag_place': max_mag_place,
        'max_mag_mag': max_mag_mag,
    }
    return render_template('index.html', context=context)

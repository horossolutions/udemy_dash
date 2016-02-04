from app import app
from .models import EarthquakeMonth, DashboardBarWidget
from flask import render_template, Markup
from nvd3 import discreteBarChart


@app.route('/')
def index():
    earthquake_month = EarthquakeMonth()
    max_mag_row = earthquake_month.max_mag_row
    max_mag_place = max_mag_row['properties.place']
    max_mag_mag = max_mag_row['properties.mag']

    df = earthquake_month.df

    x_data_alert = [int(x) for x in
        df['properties.alert'].value_counts()]
    y_data_alert = df['properties.alert'].value_counts(
        ).index

    bar_chart_alert = DashboardBarWidget(
        'bar_chart_alert', 400, 400, y_data_alert,
        x_data_alert)
    bar_chart_alert_html = bar_chart_alert.get_html()

    rounded_properties_cdi = df['properties.cdi'].round()
    cdi_value_counts = rounded_properties_cdi.value_counts()
    y_data_cdi = [int(x) for x in cdi_value_counts]
    x_data_cdi = [int(x) for x in cdi_value_counts.index]
    bar_chart_cdi = DashboardBarWidget(
        'bar_chart_cdi', 400, 400, x_data_cdi, y_data_cdi)
    bar_chart_cdi_html = bar_chart_cdi.get_html()



    context = {
        'max_mag_place': max_mag_place,
        'max_mag_mag': max_mag_mag,
        'bar_chart_alert_html': bar_chart_alert_html,
        'bar_chart_cdi_html': bar_chart_cdi_html,
    }
    return render_template('index.html', context=context)

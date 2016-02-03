from app import app
from .models import EarthquakeMonth
from flask import render_template, Markup
from nvd3 import discreteBarChart


@app.route('/')
def index():
    earthquake_month = EarthquakeMonth()
    max_mag_row = earthquake_month.max_mag_row
    max_mag_place = max_mag_row['properties.place']
    max_mag_mag = max_mag_row['properties.mag']
    bar_chart_alert_html = Markup(bar_chart_alert(
        earthquake_month.df))
    context = {
        'max_mag_place': max_mag_place,
        'max_mag_mag': max_mag_mag,
        'bar_chart_alert_html': bar_chart_alert_html,
    }
    return render_template('index.html', context=context)

def bar_chart_alert(df):
    chart_type = 'discreteBarChart'
    chart = discreteBarChart(
        name=chart_type,
        height=200,
        width=400,
        jquery_on_ready=True)

    ydata = [int(x) for x in df['properties.alert'].value_counts()]
    xdata = df['properties.alert'].value_counts().index

    chart.add_serie(y=ydata,x=xdata)
    chart.buildhtml()

    chart_html = chart.htmlcontent
    return chart_html

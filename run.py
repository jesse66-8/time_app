#jiexi_liu_lab2
from flask import Flask
from datetime import datetime, timezone, timedelta
import pytz
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_current_time():
    utc_time = datetime.now(pytz.utc)
    new_york_tz = pytz.timezone('America/New_York')
    time_newyork = utc_time.astimezone(new_york_tz)
    time_str = time_newyork.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return 'Current Time in New York: {}'.format(time_str)


app.run(host='0.0.0.0',
        port=8080,
        debug=True)

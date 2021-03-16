import requests
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///weather.db'

db=SQLAlchemy(app)
class City(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)

@app.route('/')
def index():
    cities=City.query.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=84cbf4fa48a6271f5ffa27abe197da00'
    weather_data=[]
    for city in cities:
        r=requests.get(url.format(city.name)).json()

        weather={
            'city':city,
            'temperature':r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(weather)

    return render_template('weather.html',weather_data=weather_data)











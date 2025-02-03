from flask import Flask, render_template, request
import requests

# mga import na to sa taas
# Flask for web framework
#render_template to render HTML
#request to handle HTTP requests
# imp.request para maka request ung HTML ng api

#ito ung create nugn flask class
app = Flask(__name__)

# OpenWeatherMap API Key
OPENWEATHERMAP_API_KEY = '331cf67a2586e58b0ed7d0f936bfd87e'
# Google Maps API Key
GOOGLE_MAPS_API_KEY = 'AIzaSyDOySEH_ZY73_gd0au7bek56h8msOPDqrE'



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return render_template('index.html', weather=weather_data, city=city, google_maps_api_key=GOOGLE_MAPS_API_KEY)
    return render_template('index.html', weather=None, google_maps_api_key=GOOGLE_MAPS_API_KEY)

def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'lat': data['coord']['lat'],
            'lon': data['coord']['lon']
        }
        return weather
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
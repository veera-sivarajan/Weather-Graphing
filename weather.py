import requests
import json
def get_weather():
    api_address = "api.openweathermap.org/data/2.5/weather?"
    api_id = "cc3362d516adab04bdb7ff95a68afd34"
    lat = 42.340382 
    lon = -72.496819
    location = "lat=" + str(lat) + "&" + "lon=" + str(lon) + "&units=imperial" + "&appid="
    web_url = "http://" + api_address + location + api_id
    json_data = requests.get(web_url).json()

    temperature = json_data['main']['temp']
    return temperature
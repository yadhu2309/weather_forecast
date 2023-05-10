from celery import shared_task
from .models import Weather
import requests

# # print(client)
# # #Define Db Name

# # #Define Collection

# mascot_1={
#     "name": "Sammy",
#     "type" : "Shark"
# }




base_url = 'http://api.weatherapi.com/v1/forecast.json'
api_key='1f0da2eb290a4363a6c83048230905'
cities = ["London","New York","Tokyo","Mumbai","Beijing"]


@shared_task(bind=True)
def get_weather_data(self):
    for city in cities:
        params = {
            'q':city,
            'key':api_key
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            # print(data['forecast']['forecastday'][0]['hour'])
            forecasts = data['forecast']['forecastday'][0]['hour']
            
            print(city)
            for forecast in forecasts:
                weather = Weather(city=city,date=forecast['time'],temp=forecast['temp_c'],condition=forecast['condition']['text'])
                weather.save()
                # collection.insert_one(forecast)
                print("time",forecast['time'])
                print("tmp",forecast['temp_c'])
                print("condition",forecast['condition']['text'])

    

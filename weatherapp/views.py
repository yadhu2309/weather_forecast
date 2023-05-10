from django.shortcuts import render,HttpResponse
from .tasks import get_weather_data
from .models import Weather
import time
import schedule


# client = MongoClient("mongodb://localhost:27017")
# dbname = client['admin']
# collection = dbname['weather_forecast']


# Create your views here.



# def save_data():
#     pass

def fetch_weather_data(request):
   
    # schedule.every().day.at("16:36").do(get_weather_data)
    get_weather_data.delay()
    data=Weather.objects.all()
    # print("length",data)

    return render(request,'home.html',{'context':data})

# while True:
#         schedule.run_pending()
#         time.sleep(1)
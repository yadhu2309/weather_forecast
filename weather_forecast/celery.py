import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_forecast.settings")
app = Celery("weather_forecast")
app.config_from_object("django.conf:settings", namespace="CELERY")

# celery beat  setting

app.conf.beat_schedule = {
    'get-every-day-at-6':{
        'task':'weatherapp.tasks.get_weather_data',
        'schedule':crontab(minute=0, hour=0),


        
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()
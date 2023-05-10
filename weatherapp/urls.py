from django.urls import path,include
from  . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.fetch_weather_data,name='fetch_data'),
    
]

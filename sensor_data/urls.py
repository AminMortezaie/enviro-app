from django.urls import path, include

from sensor_data import views

urlpatterns = [
    path('data/', views.SensorDataViewSet.as_view()),

]
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from weather.views import WeatherViewSet, TaskViewSet

router = DefaultRouter()
router.register("weather", WeatherViewSet)
router.register("tasks", TaskViewSet),


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "weather"

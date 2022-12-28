from django_q.models import Schedule
from django_q.tasks import async_task, fetch
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from weather.models import Weather
from weather.serializers import WeatherSerializer, TaskSerializer


class WeatherViewSet(viewsets.ModelViewSet):
    """Viewset of weather list"""

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    @action(methods=["GET"], detail=False, url_path="update-weather")
    def update_weather(self, request):
        """
        Run task for update weather information
        """
        task = fetch(async_task("weather.tasks.weather_add", sync=True))
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Viewset of tasks list"""

    queryset = Schedule.objects.all()
    serializer_class = TaskSerializer

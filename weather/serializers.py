import datetime

from django_q.models import Schedule
from rest_framework import serializers
from weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    """Serializer for the Weather model."""

    class Meta:
        model = Weather
        fields = ["date", "temperature", "weather_description"]


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Schedule model.

    The serializer will serialize the following fields:
    - 'id': the id of the schedulet task
    - 'name': the name of the schedule task
    - 'func': the function that the schedule task will execute
    - 'schedule_type': the type of schedule, either 'MINUTES' or 'CRON'
    - 'minutes': the number of minutes between each execution of the schedule (if schedule_type is 'MINUTES')
    - 'repeats': whether the schedule repeats or not
    - 'next_run': the date and time of the next scheduled task execution
    - 'cron': the cron expression defining the schedule (if schedule_type is 'CRON')

    The 'name', 'func', and 'repeats' fields are read-only.
    """

    def to_representation(self, instance):
        status = super().to_representation(instance)
        if instance.next_run.strftime(
            "%Y-%m-%dT%H:%M:%S%z"
        ) < datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"):
            status["status"] = "Done"
        elif instance.next_run.strftime(
            "%Y-%m-%dT%H:%M:%S%z"
        ) > datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"):
            status["status"] = "Scheduled"
        else:
            status["status"] = "In Progress"
        return status

    class Meta:
        model = Schedule
        fields = [
            "id",
            "name",
            "func",
            "schedule_type",
            "minutes",
            "repeats",
            "next_run",
            "cron",
        ]
        read_only_fields = [
            "name",
            "func",
            "repeats",
        ]

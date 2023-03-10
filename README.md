# Weather Parser API

API service for parse weather from https://pogoda.meta.ua/ with schedule tasks written on DRF

## Installing using Github

```shell
git clone https://github.com/KirillDrago/WeatherMeta.git
python3 -m venv venv
source venv/bin/activate (Linux and macOS) or venv\Scripts\activate (Windows)
python manage.py migrate
python manage.py runserver
```
### Run Redis with docker

Docker should be installed

```shell
docker run -d -p 6379:6379 redis
```

### Create user for admin panel
```
python manage.py createsuperuser
```

### Run parse of weather
1. Add Schedule Task from admin panel
2. Func - "weather.tasks.weather_add"
3. Choose schedule type - "Daily"
4. Choose time and date


![img.png](img.png)

### Endpoint
- /weather - list of days with weather
- /weather/update-weather - Run task for update weather information
- /tasks - list of tasks

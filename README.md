# Weather Parser API

API service for parse weather with schedule tasks written on DRF

## Installing using Github

Install PostgreSQL and create db

```shell
git clone https://github.com/KirillDrago/WeatherMeta.git
python3 -m venv venv
source venv/bin/activate (Linux and macOS) or venv\Scripts\activate (Windows)
pip install -r requirements.txt
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
python manage.py migrate
python manage.py runserver
```
### Run with docker

Docker should be installed

```shell
docker-compose build
docker-compose up
```

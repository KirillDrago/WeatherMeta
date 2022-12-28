from urllib.parse import urljoin

import cloudscraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from weather.models import Weather


BASE_URL = "https://pogoda.meta.ua/"
WEATHER_URL = urljoin(BASE_URL, "ua/Kyivska/Kyivskiy/Kyiv/")


def get_all_weather():
    """
    Scrape weather data for a week from a weather website and return it as a list of dictionaries.

    The dictionaries in the list contain the following keys:
    - 'date': a string representing the date of the weather data in the format 'YYYY-MM-DD'
    - 'temperature': a string representing the temperature in degrees Celsius
    - 'weather_description': a string describing the weather conditions, such as 'partly cloudy'

    The weather data is scraped using the Chrome webdriver and the cloudscraper library.
    """
    weather_data = []
    driver = webdriver.Chrome("../chromedriver")
    driver.get(WEATHER_URL)
    scraper = cloudscraper.create_scraper()
    week = driver.find_element(By.CLASS_NAME, "city__week-inner")
    days = week.find_elements(By.CLASS_NAME, "city__day")
    for day in days:
        day.click()
        date = day.get_property("id")
        link = scraper.get(f"{WEATHER_URL}/{date}/ajax").content
        soup = BeautifulSoup(link, "html.parser")
        weather_descriptions_selector = soup.select(".city__main-image-descr > span")
        weather_description = ", ".join(
            [i.text for i in weather_descriptions_selector]
        ).replace(".", "")
        temperature = soup.select_one(".city__main-temp").text.replace("°", "")
        weather_data.append(
            {
                "date": date,
                "temperature": temperature,
                "weather_description": weather_description,
            }
        )
    driver.close()

    return weather_data


def save_weather_data(weather_data):
    """
    Save the given weather data to the database.
    If a record with the same date already exists in the database, it will be updated with the new data.
    If no such record exists, a new record will be created.
    """
    for day in weather_data:
        weather, created = Weather.objects.get_or_create(date=day["date"])
        weather.temperature = day["temperature"]
        weather.weather_description = day["weather_description"]
        if not created:
            weather.temperature = day["temperature"]
            weather.weather_description = day["weather_description"]
        weather.save()

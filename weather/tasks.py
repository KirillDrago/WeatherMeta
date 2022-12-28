from weather.parser import save_weather_data, get_all_weather


def weather_add():
    """Calling parse weather function and save data to database"""
    save_weather_data(get_all_weather())

# weather_api_factory.py
from weather_api import OpenWeatherMapAPI
class WeatherAPIFactory:
    def create_api(self, api_type):
        if api_type == "openweathermap":
            return OpenWeatherMapAPI()
        else:
            raise ValueError(f"Unsopported API Type: {api_type}")


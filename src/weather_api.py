# weather_api.py
from abc import ABC, abstractmethod
import requests


class WeatherAPI(ABC):
    @abstractmethod
    def get_weather(self, location):
        pass


class OpenWeatherMapAPI(WeatherAPI):
    def __init__(self):
        self.api_key = "686089244d2de25a02aad24881dc95f3"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, location):
        params = {
            "q": location,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json
        else:
            raise Exception(f"Failed to fetch weather data: {response.status.code}")
        pass

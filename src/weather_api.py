# weather_api.py
from abc import ABC, abstractmethod


class WeatherAPI(ABC):
    @abstractmethod
    def get_weather(self, location):
        pass


class OpenWeatherMapAPI(WeatherAPI):
    def get_weather(self, location):
        # Implement OpenWeatherMap API call
        pass

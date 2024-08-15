# weather_display.py
from abc import ABC, abstractmethod

class WeatherDisplay(ABC):
    @abstractmethod
    def show(self, data):
        pass

class TemperatureDisplay(WeatherDisplay):
    def show(self, data):
        # Display temperature data
        pass

class HumidityDisplay(WeatherDisplay):
    def show(self, data):
        # Display humidity data
        pass


# weather_data_fetcher.py

from weather_api_factory import WeatherAPIFactory


class WeatherDataFetcher:
    def __init__(self):
        self.api_factory = WeatherAPIFactory()

    def fetch_data(self, location):
        """
        Fetch weather data using appropriate API.

        Examples:
        >>> fetcher = WeatherDataFetcher()
        >>> data = fetcher.fetch_data("New York")
        >>> isinstance(data, dict)
        True
        """
        # For the purpose of the example, let's return a mock dictionary
        return {
            "location": location,
            "temperature": 22.5,
            "humidity": 60
        }

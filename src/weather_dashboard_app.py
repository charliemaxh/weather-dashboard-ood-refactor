# weather_dashboard_app.py
import tkinter as tk
from weather_data_fetcher import WeatherDataFetcher
from weather_data_processor import WeatherDataProcessor
from weather_visualizer import WeatherVisualizer
from weather_display_factory import WeatherDisplayFactory

class WeatherDashboardApp:
    def __init__(self):
        self.root = tk.Tk()
        self.data_fetcher = WeatherDataFetcher()
        self.data_processor = WeatherDataProcessor()
        self.visualizer = WeatherVisualizer()
        self.display_factory = WeatherDisplayFactory()

    def run(self):
        location = "Perth"
        raw_data = self.data_fetcher.fetch_data(location)
        processed_data = self.data_processor.process_data(raw_data)

        print(processed_data)        
        pass


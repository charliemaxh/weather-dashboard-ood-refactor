# weather_dashboard_app.py
class WeatherDashboardApp:
    def __init__(self):
        self.root = tk.Tk()
        self.data_fetcher = WeatherDataFetcher()
        self.data_processor = WeatherDataProcessor()
        self.visualizer = WeatherVisualizer()
        self.display_factory = WeatherDisplayFactory()

    def run(self):
        # Main application logic here
        pass


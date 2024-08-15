import sys
import os
import doctest

# Adjust PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

import weather_data_fetcher


def run_all_doctests():
    doctest.testmod(weather_data_fetcher)

if __name__ == "__main__":
    run_all_doctests()

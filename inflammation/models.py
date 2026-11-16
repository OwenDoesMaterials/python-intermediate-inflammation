"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def load_json(filename):
    """Load a numpy array from a JSON document.

    Expected format:
    [
      {
        "observations": [0, 1]
      },
      {
        "observations": [0, 2]
      }    
    ]
    :param filename: Filename of CSV to load
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)


class CSVDataSource():
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        """Loads all csv data from a given directory

            Args:
                data_dir (string): directory of csvs
            """
        file_paths = glob.glob(os.path.join(
            self.data_source, 'inflammation-*.csv'))
        if len(file_paths) == 0:
            raise ValueError(
                f"No CSV files found in path {self.data_source}")
        data = map(models.load_csv, file_paths)
        return list(data)


class JSONDataSource():
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        """Loads all JSON data from a given directory
            Args:
                data_dir (string): directory of JSON
            """
        file_paths = glob.glob(os.path.join(
            self.data_source, 'inflammation-*.json'))
        if len(file_paths) == 0:
            raise ValueError(
                f"No json files found in path {self.data_source}")
        data = map(models.load_json, file_paths)
        return list(data)

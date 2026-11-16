"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


class AbstractDataSource():
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(data_dir):
        pass


def load_data(data_dir):
    """Loads all csv data from a given directory

    Args:
        data_dir (string): directory of csvs
    """
    data_file_paths = glob.glob(os.path.join(data_dir, '*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(
            f"No CSV files found in path {data_dir}")
    data = map(models.load_csv, data_file_paths)
    return list(data)


def analyse_data(data):
    """Calculates and plots mean inflammation data and standard deviations
    Use as analyse_data(load_data(directory))
    Args:
        data (list: output of load_data)
    """
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)

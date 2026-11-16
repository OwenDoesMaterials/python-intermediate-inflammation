"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


def analyse_data(data_source):
    """Calculates and plots mean inflammation data and standard deviations
    Use as analyse_data(load_data(directory))
    """
    data = data_source.load_data()
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)

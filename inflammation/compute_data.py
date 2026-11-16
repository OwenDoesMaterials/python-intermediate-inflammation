"""Module containing mechanism for calculating standard deviation between datasets.
"""

import os
import numpy as np

from inflammation import models, views


def analyse_data(data):
    """Calculates and plots mean inflammation data and standard deviations
    Use as analyse_data(load_data(directory))
    """
    means_by_day = map(models.daily_mean, data)  # model
    means_by_day_matrix = np.stack(list(means_by_day))  # model
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)  # model

    return daily_standard_deviation

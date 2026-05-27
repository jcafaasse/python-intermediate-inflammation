"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np

class Patient:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def get_body_mass_index(self):
        """Compute body mass index
        """        
        return self.weight / self.height**2

def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data: np.ndarray) -> np.ndarray:
    """Calculate the daily mean of a 2d inflammation data array.

    :param data: 2d inflammation data array (each row is a patient, each column is a day)
    :return array of daily means, one for each day (column) in the input data
    """
    return np.mean(data, axis=0)


def daily_max(data: np.ndarray) -> np.ndarray:
    """Calculate the daily max of a 2d inflammation data array

    :param data: 2d inflammation data array (each row is a patient, each column is a day)
    :return: array of daily maxima, one for each day (column) in the input data
    """    
    return np.max(data, axis=0)


def daily_min(data: np.ndarray) -> np.ndarray:
    """Calculate the daily min of a 2d inflammation data array

    :param data: 2d inflammation data array (each row is a patient, each column is a day)
    :return: array of daily minima, one for each day (column) in the input data
    """    
    return np.min(data, axis=0)


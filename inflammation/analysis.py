"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np
import argparse
import json

from inflammation import models, views

class JSONDataSource:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def load_json(self, filename):
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
        with open(file=filename, mode='r', encoding='utf-8') as file:
            data_as_json = json.load(file)
            return [np.array(entry['observations']) for entry in data_as_json]
        
    def load_inflammation_data(self):
        """Loads 

        :param data_dir: directory containing inflammation JSON files
        :raises ValueError: when no inflammation JSON files are found in data_dir
        :return: combined data
        """    
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.data_dir}")
        data = map(self.load_json, data_file_paths)
        return data



class CSVDataSource:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir


    def load_inflammation_data(self):
        """Loads 

        :param data_dir: directory containing inflammation CSV files
        :raises ValueError: when no inflammation CSV files are found in data_dir
        :return: combined data
        """    
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        data = map(models.load_csv, data_file_paths)
        return data

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = data_source.load_inflammation_data()
    print(data)
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    return daily_standard_deviation

def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation

if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Calculate standard deviation by day between datasets."
    )
    
    # Add the data_dir argument
    parser.add_argument(
        'data_dir', 
        type=str, 
        help="Path to the directory containing the inflammation CSV files."
    )
    
    # Parse the arguments from the command line
    args = parser.parse_args()
    
    # Run the function using the provided argument
    data_source = CSVDataSource(args.data_dir)
    analyse_data(data_source)
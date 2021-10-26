import pandas as pd
import numpy as np
import json

from pandas.core.frame import DataFrame
from pandas.io.clipboards import read_clipboard

class Preprocessor:

    # empty constructor
    def __init__(self) -> None:
        pass

    # helper function
    def read_dataset(self, path_of_file: str): # returns file as python object
        with open(path_of_file) as json_file:
            return json.load(json_file)

    # helper functions
    def transform_range(self, entry: dict): # This function returns the average of a range (for impressions and spend)
        lower = entry["lower_bound"]
        if entry.get("upper_bound") == None:
            higher = entry["lower_bound"]
        else:
            higher = entry["upper_bound"]
        return int(int(lower) + int(higher)) / 2

    def json_to_python(self, dict_string): # Transoforms spend and impressions back to dictionnaries when reading from csv
        # Convert to proper json format
        js_string = dict_string.replace("'", '"')
        return json.loads(js_string) # loads json string

    # preprocessing functions
    def file_to_df(self, path: str) -> pd.DataFrame: # transforms json file into usable format
        
        file = pd.DataFrame(self.read_dataset(path))
        # transform spend & impression ranges into average
        file["spend"] = file["spend"].apply(lambda x: self.transform_range(x))
        file["impressions"] = file["impressions"].apply(lambda x: self.transform_range(x))
        # transform into datetime
        file["ad_creation_time"] = pd.to_datetime(file["ad_creation_time"])
        return file

import pandas as pd
import numpy as np
import json

from pandas.core.frame import DataFrame

class Preprocessor:

    # empty constructor
    def __init__(self) -> None:
        pass

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
        return json.loads(js_string)

    # preprocessing functions
    def transform_csv(self, path: str) -> pd.DataFrame: # transforms csv into usable format
        file = pd.read_csv(path)
        # transform spend & impression into ranges
        file["spend"] = file["spend"].apply(lambda x: self.json_to_python(x)).apply(lambda x: self.transform_range(x))
        file["impressions"] = file["impressions"].apply(lambda x: self.json_to_python(x)).apply(lambda x: self.transform_range(x))
        # # transform json strings into python objects
        file["delivery_by_region"] = file["delivery_by_region"].apply(lambda x: self.json_to_python(x) if not pd.isnull(x) else np.nan)
        file["demographic_distribution"] = file["demographic_distribution"].apply(lambda x: self.json_to_python(x) if not pd.isnull(x) else np.nan)
        # datetime
        file["ad_creation_time"] = pd.to_datetime(file["ad_creation_time"])
        return file

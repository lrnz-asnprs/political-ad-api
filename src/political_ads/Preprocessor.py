import pandas as pd
import numpy as np
import json
import os
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
    def avg_range(self, entry: dict): # This function returns the average of a range (for impressions and spend)
        lower = entry["lower_bound"]
        if entry.get("upper_bound") == None:
            higher = entry["lower_bound"]
        else:
            higher = entry["upper_bound"]
        return int(int(lower) + int(higher)) / 2

    # merge all single files into one bigger!
    def merge_files(self, directory: str):
        dir = r'single_files'
        final_list = []
        files = set() # iterate over files in that directory and put in set
        for filename in os.listdir(dir):
            print(filename)
                    # checking if it is a file
            if filename.endswith("txt"):
                    files.add(filename)
        while len(files) > 0:
            file = files.pop()
            try:
                print(dir + "\\" + file)
                joined_path = dir + "\\" + file
                data = self.read_dataset(joined_path)
                final_list.extend(data) # concatenate data to list
                print(len(final_list))
            except:
                files.add(file) # add file back
                print(f"There was an error with file {file}")

        jsonFile = open("data\\all_politicians_aggregated.txt", "w") # filepath and name specified here!
        final_file_str = json.dumps(final_list)
        jsonFile.write(final_file_str)
        jsonFile.close()

    def merge_files_gg(self, directory: str):
        dir = r'single_files'
        final_list = []
        files = set() # iterate over files in that directory and put in set
        for filename in os.listdir(dir):
            print(filename)
                    # checking if it is a file
            if filename.endswith("txt"):
                    files.add(filename)
        while len(files) > 0:
            file = files.pop()
            try:
                print(dir + "/" + file)
                joined_path = dir + "/" + file
                data = self.read_dataset(joined_path)
                final_list.extend(data) # concatenate data to list
                print(len(final_list))
            except:
                files.add(file) # add file back
                print(f"There was an error with file {file}")

        jsonFile = open("data/all_politicians_aggregated.txt", "w") # filepath and name specified here!
        final_file_str = json.dumps(final_list)
        jsonFile.write(final_file_str)
        jsonFile.close()



    def upper_bound(self, entry: dict): # This function returns the average of a range (for impressions and spend)
        if entry.get("upper_bound") == None:
            higher = entry["lower_bound"]
        else:
            higher = entry["upper_bound"]
        return int(higher)

    def json_to_python(self, dict_string): # Transoforms spend and impressions back to dictionnaries when reading from csv
        # Convert to proper json format
        js_string = dict_string.replace("'", '"')
        return json.loads(js_string) # loads json string

    # preprocessing functions
    def file_to_df(self, path: str) -> pd.DataFrame: # transforms json file into usable format
        file = pd.DataFrame(self.read_dataset(path))
        # create upper and lower boundaries
        file["spend_lo"] = file["spend"].apply(lambda x: int(x["lower_bound"]))
        file["spend_hi"] = file["spend"].apply(lambda x: self.upper_bound(x))
        file["impressions_lo"] = file["impressions"].apply(lambda x: int(x["lower_bound"]))   
        file["impressions_hi"] = file["impressions"].apply(lambda x: self.upper_bound(x))   
        # transform spend & impression ranges into average
        file["spend"] = file["spend"].apply(lambda x: self.avg_range(x))
        file["impressions"] = file["impressions"].apply(lambda x: self.avg_range(x))
        # transform into datetime
        file["ad_creation_time"] = pd.to_datetime(file["ad_creation_time"])
        return file


    def group_by_pages(self, data: pd.DataFrame) -> pd.DataFrame:    
        '''
        Amount spend by facebook page
        '''
        by_page = data.groupby("page_name").agg(
            # Aggregate no of ads
            no_ads = ('id', 'count'),
            # Aggregate sum of spend & total impressions generated
            spend_lo = ('spend_lo', 'sum'),
            spend_hi = ('spend_hi', 'sum'),
            impressions_lo = ('impressions_lo', 'sum'),
            impressions_hi = ('impressions_hi', 'sum'),
            # Average number of impressions & spend per ad
            avg_impressions = ('impressions', 'mean'),
            avg_spend = ('spend', 'mean')

        ).reset_index()
        
        return by_page

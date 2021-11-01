from facebook_scraper import get_page_info
import time
import pandas as pd
import numpy as np

'''
This script scrapes the fb-page info for the given politicians and saves results as csv

'''
# Helper
def get_page_id(data: pd.DataFrame, name: str):
    match = data[data["Page Name"].str.contains(name, na=False)]
    if len(match) != 0:
        return match.iloc[0][0]
    else:
        return "no match"


# Main script
congress_members = pd.DataFrame(pd.read_csv("..\\src\\data_sets\\legislators-current.csv"))
report = pd.read_csv("..\\data\\FacebookAdLibraryReport_2021-10-15_US_lifelong_advertisers.csv")
members_fbNames_test = [] # list of tuples

for value in congress_members["facebook"].items():
    if not pd.isnull(value[1]):
        page = get_page_info(account=value[1])
        print(page)
        if "name" and "identifier" in page:
            members_fbNames_test.append((value[1], page["name"], page["identifier"]))
            print(page["name"] + " id:" + str(page["identifier"]))
    time.sleep(0.5)

members_names = pd.DataFrame(members_fbNames_test, columns=["facebook", "page_name", "identifier"])

congress_members_fb = congress_members[["first_name", "last_name", "full_name", "type", "state", "district", "party", "facebook"]]

merged = congress_members_fb.merge(right=members_names, on="facebook", how="left")

# inserts page ids from report file
merged["page_id"] = merged.apply(lambda x: get_page_id(report,x["full_name"]),axis=1)

merged["identifier"] = merged["identifier"].fillna(0).astype(np.int64)

merged.to_csv("..\\src\\data_sets\\legislators_facebookdata.csv", index=False, header=True)

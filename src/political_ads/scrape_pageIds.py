from facebook_scraper import get_page_info
import time
import pandas as pd
import numpy as np

'''
This script scrapes the fb-page info for the given politicians and saves results as csv
'''

congress_members = pd.DataFrame(pd.read_csv("..\\src\\data_sets\\legislators-current.csv"))
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

merged["identifier"] = merged["identifier"].fillna(0).astype(np.int64)

merged.to_csv("..\\src\\data_sets\\legislators_fb_info.csv", index=False, header=True)







# Save data as csv
members_names.to_csv("..\\src\\data_sets\\legislators_page_ids.csv", index=False, header=True)

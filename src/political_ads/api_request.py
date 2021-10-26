import requests
import numpy as np
import pandas as pd
from political_ads.helper import *
import time
import json

class API_request:

    def __init__(self) -> None:
        pass

    # helper method
    def get_json_response(self, url, token):
        headers = {"Authorization": "Bearer {}".format(token)}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def generate_dataset(self, limit_per_call: int, search_terms: str, access_token: str): # insert your access token here (expires every 2 hours)
        
        # PARAMETERS NECESSARY
        ad_type = "POLITICAL_AND_ISSUE_ADS"
        ad_reached_countries = ['US'] # Facebook delivered the ads in these countries. Provided as ISO country codes.
        search_terms = search_terms # The terms to search for in your query. We treat a blank space as a logical AND and search for both terms and no other operators. The limit of your string is 100 characters or less.
        limit = limit_per_call

        # FIELDS to specify your results
        fields = ["ad_creation_time", "ad_creative_body","spend", "impressions", "delivery_by_region", "demographic_distribution","page_id", "page_name","bylines","id"]

        # see here for more parameters and fields: https://www.facebook.com/ads/library/api/?source=archive-landing-page 

        input_url = f"https://graph.facebook.com/v12.0/ads_archive?search_terms={search_terms}&ad_type={ad_type}&ad_reached_countries={ad_reached_countries}&fields={fields}&limit={limit}"

        response = self.get_json_response(input_url, access_token) # generate first response

        counter = 0
        final_response = response["data"] # final response python list initialized and add first result

        while "next" in response["paging"]:
            response = self.get_json_response(response["paging"]["next"], access_token)
            final_response.extend(response["data"]) # add the results to final list
            counter += 1
            time.sleep(5)
            print(f"Iteration number {counter} and amount of data: {counter * 500}")

        # when loop has finished, then store result in file
        final_str = json.dumps(final_response) # store as json string
        jsonFile = open("..\\data\\generated_dataset.txt", "w") # open file
        jsonFile.write(final_str) # write to file
        jsonFile.close()


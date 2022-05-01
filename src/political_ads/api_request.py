import requests
import numpy as np
import pandas as pd
# from political_ads.helper import *
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


    # generate single json files for each congress member in the list
    def create_single_files(self, token, congress_members: pd.DataFrame):

        pid_list = congress_members[congress_members["page_id"] != "no match"]["page_id"].tolist()
        congress_members_pid_set = set(pid_list) # make set of page ids

        while len(congress_members_pid_set) > 0:
            p_id = congress_members_pid_set.pop() # get next page_id
            politician = congress_members[congress_members["page_id"] == p_id]  # get corresponding entry in df
            politician_name = politician.full_name.values[0].replace(" ", "_") # name of politician
            try:
                print(f"Try politician {politician_name} ") 
                ads_data = self.dataset_by_pageId_asString(500, [p_id], token)
                final_str = json.dumps(ads_data) 
                jsonFile = open(f"..\\single_files\\{politician_name}_{p_id}.txt", "w") # filepath and name specified here!
                jsonFile.write(final_str)
                jsonFile.close()
                print(f"Successfully created file for {politician_name}. Length of set is now: {len(congress_members_pid_set)}")
            except:
                congress_members_pid_set.add(p_id) # add element back to set and try again
                print(f"Error occured for politician {politician_name} with page_id {p_id}")
                pass


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

        while "paging" in response:  
            while "next" in response["paging"]:
                if counter == 2:
                    break
                response = self.get_json_response(response["paging"]["next"], access_token)
                final_response.extend(response["data"]) # add the results to final list
                counter += 1
                time.sleep(5)
                print(f"Iteration number {counter} and amount of data: {counter * limit_per_call}")
                if "paging" not in response:
                    break

        final_str = json.dumps(final_response) 
        jsonFile = open("..\\data\\generated_dataset.txt", "w") # filepath and name specified here!
        jsonFile.write(final_str)
        jsonFile.close()


    #page_ids must be list of ids
    def generate_dataset_by_pageId(self, limit_per_call, page_ids, access_token): # insert your access token here (expires every 2 hours)
        
        # PARAMETERS NECESSARY
        ad_type = "POLITICAL_AND_ISSUE_ADS"
        ad_reached_countries = ['US'] # Facebook delivered the ads in these countries. Provided as ISO country codes.
        search_terms = "" # The terms to search for in your query. We treat a blank space as a logical AND and search for both terms and no other operators. The limit of your string is 100 characters or less.
        limit = limit_per_call
        search_page_ids = page_ids

        # FIELDS to specify your results
        fields = ["ad_creation_time", "ad_creative_body","spend", "impressions", "delivery_by_region", "demographic_distribution","page_id", "page_name","bylines","id"]

        # see here for more parameters and fields: https://www.facebook.com/ads/library/api/?source=archive-landing-page 

        input_url = f"https://graph.facebook.com/v12.0/ads_archive?search_terms={search_terms}&ad_type={ad_type}&ad_reached_countries={ad_reached_countries}&search_page_ids={search_page_ids}&fields={fields}&limit={limit}"

        response = self.get_json_response(input_url, access_token) # generate first response

        counter = 0
        final_response = response["data"] # final response python list initialized and add first result
                
        while "paging" in response:  
            # if counter == 1:
            #         break
            while "next" in response["paging"]:
                # if counter == 1:
                #     break
                response = self.get_json_response(response["paging"]["next"], access_token)
                final_response.extend(response["data"]) # add the results to final list
                counter += 1
                time.sleep(5)
                print(f"Iteration number {counter} and amount of data: {counter * limit_per_call}")
                if "paging" not in response:
                    break

        final_str = json.dumps(final_response) 
        jsonFile = open("..\\data\\dataset_by_pageId.txt", "w") # filepath and name specified here!
        jsonFile.write(final_str)
        jsonFile.close()


    # This method appends the dataset generated to an existing one!!
    def append_dataset_by_pageId(self, limit_per_call: int, page_ids: list, access_token: str): # insert your access token here (expires every 2 hours)
        
        # PARAMETERS NECESSARY
        ad_type = "POLITICAL_AND_ISSUE_ADS"
        ad_reached_countries = ['US'] # Facebook delivered the ads in these countries. Provided as ISO country codes.
        search_terms = "" # The terms to search for in your query. We treat a blank space as a logical AND and search for both terms and no other operators. The limit of your string is 100 characters or less.
        limit = limit_per_call
        search_page_ids = page_ids

        # FIELDS to specify your results
        fields = ["ad_creation_time", "ad_creative_body","spend", "impressions", "delivery_by_region", "demographic_distribution","page_id", "page_name","bylines","id"]

        # see here for more parameters and fields: https://www.facebook.com/ads/library/api/?source=archive-landing-page 

        input_url = f"https://graph.facebook.com/v12.0/ads_archive?search_terms={search_terms}&ad_type={ad_type}&ad_reached_countries={ad_reached_countries}&search_page_ids={search_page_ids}&fields={fields}&limit={limit}"

        response = self.get_json_response(input_url, access_token) # generate first response

        counter = 0
        final_response = response["data"] # final response python list initialized and add first result
                
        while "paging" in response:  
            # if counter == 1:
            #         break
            while "next" in response["paging"]:
                # if counter == 1:
                #     break
                response = self.get_json_response(response["paging"]["next"], access_token)
                final_response.extend(response["data"]) # add the results to final list
                counter += 1
                time.sleep(5)
                print(f"Iteration number {counter} and amount of data: {counter * limit_per_call}")
                if "paging" not in response:
                    break

        # final_str = json.dumps(final_response) 

        # load existing file
        with open('..\\data\\dataset_by_pageId_appended.txt') as f:
            existing_file = json.load(f)

        existing_file.extend(final_response) # add string to file

        jsonFile = open("..\\data\\dataset_by_pageId_appended.txt", "w") # filepath and name specified here!

        final_file_str = json.dumps(existing_file)
        jsonFile.write(final_file_str)
        jsonFile.close()


    # This method returns a json string of ALL ads by one page_id!
    def dataset_by_pageId_asString(self, limit_per_call: int, page_ids: list, access_token: str): # insert your access token here (expires every 2 hours)
        # PARAMETERS NECESSARY
        ad_type = "POLITICAL_AND_ISSUE_ADS"
        ad_reached_countries = ['US'] # Facebook delivered the ads in these countries. Provided as ISO country codes.
        search_terms = "" # The terms to search for in your query. We treat a blank space as a logical AND and search for both terms and no other operators. The limit of your string is 100 characters or less.
        limit = limit_per_call
        search_page_ids = page_ids

        # FIELDS to specify your results
        fields = ["ad_creation_time", "ad_creative_body","spend", "impressions", "delivery_by_region", "demographic_distribution","page_id", "page_name","bylines","id"]

        # see here for more parameters and fields: https://www.facebook.com/ads/library/api/?source=archive-landing-page 

        input_url = f"https://graph.facebook.com/v12.0/ads_archive?search_terms={search_terms}&ad_type={ad_type}&ad_reached_countries={ad_reached_countries}&search_page_ids={search_page_ids}&fields={fields}&limit={limit}"

        response = self.get_json_response(input_url, access_token) # generate first response

        counter = 0
        final_response = response["data"] # final response python list initialized and add first result
                
        while "paging" in response:  
            # if counter == 1:
            #         break
            while "next" in response["paging"]:
                # if counter == 1:
                #     break
                response = self.get_json_response(response["paging"]["next"], access_token)
                final_response.extend(response["data"]) # add the results to final list
                counter += 1
                time.sleep(5)
                print(f"Iteration number {counter} and amount of data: {counter * limit_per_call}")
                if "paging" not in response:
                    break

        # final_str = json.dumps(final_response) 

        return final_response
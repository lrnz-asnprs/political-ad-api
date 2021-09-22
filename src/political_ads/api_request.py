import requests

# insert your access token here (expires every 2 hours)
access_token = ""

# PARAMETERS NECESSARY
ad_type = "POLITICAL_AND_ISSUE_ADS"
ad_reached_countries = ['US', 'DE'] # Facebook delivered the ads in these countries. Provided as ISO country codes.
search_terms = "climate" # The terms to search for in your query. We treat a blank space as a logical AND and search for both terms and no other operators. The limit of your string is 100 characters or less.

# FIELDS to specify your results
fields = ["id", "ad_creative_body", "delivery_by_region", "demographic_distribution"]

# see here for more parameters and fields: https://www.facebook.com/ads/library/api/?source=archive-landing-page 

input_url = f"https://graph.facebook.com/v12.0/ads_archive?search_terms={search_terms}&ad_type={ad_type}&ad_reached_countries={ad_reached_countries}&fields={fields}"

def get_json_response(url, token):
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()



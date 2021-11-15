import pandas as pd
from pandas.core.frame import DataFrame

class Grouper:

    def __init__(self) -> None:
        pass

    # Groupy by page and returns spend and impression metrics
    def spend_impressions_by_pages(self, data: pd.DataFrame) -> pd.DataFrame:    
        '''
        Amount spend by facebook page
        '''
        by_page = data.groupby("page_name").agg(
            # Aggregate no of ads
            no_ads = ('id', 'count'),
            # Aggregate sum of spend & total impressions generated
            spend_lo = ('spend_lo', 'sum'),
            spend_hi = ('spend_hi', 'sum'),
            spend = ('spend', 'sum'),
            impressions_lo = ('impressions_lo', 'sum'),
            impressions_hi = ('impressions_hi', 'sum'),
            impressions = ('impressions', 'sum')

        ).reset_index()
        
        return by_page


    # Takes as input dataframe containing ads and groups them by day
    def group_ads_by_day(self, data: pd.DataFrame) -> pd.DataFrame:

        by_day = data.groupby("ad_creation_time").agg(
            # Aggregate no of ads
            no_ads = ('id', 'count'),
            # Aggregate sum of spend & total impressions generated
            sum_spend_lo = ('spend_lo', 'sum'),
            sum_spend_hi = ('spend_hi', 'sum'),
            median_spend = ('spend', 'median'),
            avg_spend = ('spend', 'sum'),
            sum_impressions_lo = ('impressions_lo', 'sum'),
            sum_impressions_hi = ('impressions_hi', 'sum'),
            # Average number of impressions & spend per ad
            avg_impressions = ('impressions', 'sum')

        ).reset_index().sort_values(by="ad_creation_time", ascending=True)

        return by_day

    # Takes as input dataframe containing ads and groups them by day
    def group_ads_by_page(self, data: pd.DataFrame) -> pd.DataFrame:

        by_page = data.groupby(["page_id", "page_name"]).agg(
            # Aggregate no of ads
            no_ads = ('id', 'count'),
            # Aggregate sum of spend & total impressions generated
            sum_spend_lo = ('spend_lo', 'sum'),
            sum_spend_hi = ('spend_hi', 'sum'),
            median_spend = ('spend', 'median'),
            avg_spend = ('spend', 'sum'),
            sum_impressions_lo = ('impressions_lo', 'sum'),
            sum_impressions_hi = ('impressions_hi', 'sum'),
            # Average number of impressions & spend per ad
            avg_impressions = ('impressions', 'sum')
        ).reset_index()

        congress = pd.read_csv("..\\src\\data_sets\\legislators_fb_info_final.csv") # read congress member info
        by_page["party"] = by_page["page_id"].apply(lambda x: congress[congress["page_id"] == x]["party"].values[0]) # add party to pages

        return by_page


    # Takes as input dataframe containing ads and groups them by day
    def group_ads_by_party_by_day(self, data: pd.DataFrame, party: str) -> pd.DataFrame:

        congress = pd.read_csv("..\\src\\data_sets\\legislators_fb_info_final.csv") # read congress member info
        
        party_members = congress[congress["party"] == party]  # get all page id's that match the given party

        data_party_members = data[data.page_id.isin(party_members.page_id)] # get all the ads where page id matches with the party page id's

        data_party_by_day = self.group_ads_by_day(data_party_members) # group those ads by day

        return data_party_by_day

    # Takes as input dataframe containing ads and groups them by day
    def group_ads_by_party_by_page(self, data: pd.DataFrame, party: str) -> pd.DataFrame:

        congress = pd.read_csv("..\\src\\data_sets\\legislators_fb_info_final.csv") # read congress member info
        
        party_members = congress[congress["party"] == party]  # get all page id's that match the given party

        data_party_members = data[data.page_id.isin(party_members.page_id)] # get all the ads where page id matches with the party page id's

        data_party_by_day = self.group_ads_by_page(data_party_members) # group those ads by day

        return data_party_by_day







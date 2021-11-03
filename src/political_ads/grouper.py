import pandas as pd

class Grouper:

    def __init__(self) -> None:
        pass

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
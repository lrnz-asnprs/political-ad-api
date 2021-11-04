import pandas as pd

class Filter:

    def __init__(self) -> None:
        pass

    # returns true if ad IS climate related
    def check_for_climate_ad(self, text: str): # returns true if climate related keyword contained, false otherwise
        text_lower = text.lower()
        return ("climate" in text_lower) | (("global" in text_lower) and ("warming" in text_lower)) and (("business climate" not in text_lower) | ("economic climate" not in text_lower)) 

    # returns true if ad is NOT climate related (INVERSE of the above method!)
    def check_for_NON_climate_ad(self, text: str): # returns true if climate related keyword contained, false otherwise
        text_lower = text.lower()
        return not ("climate" in text_lower) | (("global" in text_lower) and ("warming" in text_lower)) and (("business climate" not in text_lower) | ("economic climate" not in text_lower)) 

    # main function to return dataframe with climate ads
    def get_climate_ads(self, data: pd.DataFrame) -> pd.DataFrame:
        climate_ads = data[data.apply(lambda x: self.check_for_climate_ad(str(x["ad_creative_body"])),axis=1)] # returns the rows that return true
        return climate_ads
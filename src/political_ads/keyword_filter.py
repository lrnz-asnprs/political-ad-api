import pandas as pd

class Filter:

    def __init__(self) -> None:
        pass

    # helper function
    def check_for_climate_ad(self, text: str): # returns true if climate related keyword contained, false otherwise
        # text_lower = list((map(lambda x: x.lower(), text)))
        text_lower = text.lower()
        return ("climate" in text_lower) | (("global" in text_lower) and ("warming" in text_lower)) and (("business climate" not in text_lower) | ("economic climate" not in text_lower)) 

    # main function to return dataframe with climate ads
    def get_climate_ads(self, data: pd.DataFrame) -> pd.DataFrame:
        climate_ads = data[data.apply(lambda x: self.check_for_climate_ad(str(x["ad_creative_body"])),axis=1)] # returns the rows that return true
        return climate_ads
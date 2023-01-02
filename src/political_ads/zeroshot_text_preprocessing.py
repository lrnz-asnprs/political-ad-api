import re
import pandas as pd


# Remove links
def clean_data(dataframe):
#replace URL of a text
    dataframe['clean_text'] = dataframe['ad_creative_body'].str.replace('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ')
    return dataframe


# Remove emojis characters
def remove_emojis(data):
    try:
      emoj = re.compile("["
          u"\U0001F600-\U0001F64F"  # emoticons
          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
          u"\U0001F680-\U0001F6FF"  # transport & map symbols
          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
          u"\U00002500-\U00002BEF"  # chinese char
          u"\U00002702-\U000027B0"
          u"\U00002702-\U000027B0"
          u"\U000024C2-\U0001F251"
          u"\U0001f926-\U0001f937"
          u"\U00010000-\U0010ffff"
          u"\u2640-\u2642" 
          u"\u2600-\u2B55"
          u"\u200d"
          u"\u23cf"
          u"\u23e9"
          u"\u231a"
          u"\ufe0f"  # dingbats
          u"\u3030"
                        "]+", re.UNICODE)
      return re.sub(emoj, '', data)
    except:
      return data

def remove_punctuations(text):
    return re.sub('[^A-Za-z0-9]+', ' ', text)
  
  #Consider stemming and lemmatizing
def zeroshot_preprocess(input: pd.DataFrame) -> pd.DataFrame:
  
  """makes the df ready by lowercasing, removing emojis and numbers"""
  output = input.copy()
  
  output["clean_text"] = output["clean_text"].str.lower()
  output["clean_text"] = output["clean_text"].map(remove_emojis)
  output["clean_text"] = output["clean_text"].map(remove_punctuations)
  
  return output

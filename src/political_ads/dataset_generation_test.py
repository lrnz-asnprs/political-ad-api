# import sys
# sys.path.append('../src') 

from api_request import API_request
import pandas as pd


requestor = API_request()

congress = pd.read_csv("..\\data_sets\\legislators_fb_info.csv")

count = 0
while count < 20:
    query = []
    for i in range(10):
        if count < len(congress):
            query.append(congress.loc[count]["page_id"])
            count +=1
    # clean query / remove "no match"
    clean_query = []
    for i in range(len(query)):
        if query[i] != "no match":
            clean_query.append(query[i])

    requestor.append_dataset_by_pageId(500, clean_query, "EAAD3So8oorMBAPcQZCsrdT0p2lsvUuyLQozbZCnvnJnmZCeswClj2dXakZCMkPZB8B0m3qf2Ynojj31VzBZBZBd31KuUhNr1ukt9tilFGyFNhbZB4ak36zvz8LOH165dAXvmZCqbtjjvgZAXb4PbJ0ICuVpPrb9y9MqZBvk7EswvSvBCS4LXTZBEFowcoNYXZBZBuf7Ll09kPzLBsAOvktd3EepEMqsMOryyE2ZBvcudXeXB7ZCoFgeLSlDoHbNpsikZASAFriewZD")
import pandas as pd
from facebook_scraper import get_page_info


politicians_fb = pd.read_csv("src/data_sets/legislators-current.csv")

def get_pol_fbpage_names(as_set=False, as_list=False):
    
    pol_fb = politicians_fb['facebook']
    pol_fb.dropna(inplace=True)

    #default returns the list of fb page names of politicians as a set:
    if(as_set == True):
        pol_fb_set = set()

        for row in pol_fb:
            pol_fb_set.add(row)
        return pol_fb_set
    
    if(as_list == True):
        pol_fb_list = []

        for row in pol_fb:
            pol_fb_list.append(row)
        
        return pol_fb_list

    else:
        return pol_fb

def get_pol_full_names(as_set=True):

    pol_fb = politicians_fb['full_name']
    pol_fb.dropna(inplace=True)

    #default returns the list of fb page names of politicians as a set:
    if(as_set == True):
        pol_fb_set = set()

        for row in pol_fb:
            pol_fb_set.add(row)
        return pol_fb_set
    
    #otherwise one can set as_set=False and get it as a DF
    else:
        return pol_fb

list = get_pol_fbpage_names(as_list=True)


for i in list:
    print(get_page_info(account=i))


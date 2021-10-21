import pandas as pd

politicians_fb = pd.read_csv("src/data_sets/legislators-current.csv")

def get_pol_fbpage_names(as_set=True):
    
    pol_fb = politicians_fb['facebook']
    pol_fb.dropna(inplace=True)

    #default returns the list of fb page names of politicians as a set:
    if(as_set == True):
        pol_fb_set = set()

        for row in pol_fb:
            pol_fb_set.add(row)
        return pol_fb_set
    
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


test = get_pol_full_names()
print(test)

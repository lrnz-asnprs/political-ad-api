#Backup of earlier implementation for filtering geographic data.
counter_unknown = 0
lst_of_failed = []

def get_states_data(row):
    
    states_lst = []
    
    #All 50 US states ready for:
    states = {
    "Alabama": 0.0,
    "Alaska": 0.0,
    "Arizona": 0.0,
    "Arkansas": 0.0,
    "California": 0.0,
    "Colorado": 0.0,
    "Connecticut": 0.0,
    "Delaware": 0.0,
    "Florida": 0.0,
    "Georgia": 0.0,
    "Hawaii": 0.0,
    "Idaho": 0.0,
    "Illinois": 0.0,
    "Indiana": 0.0,
    "Iowa": 0.0,
    "Kansas": 0.0,
    "Kentucky": 0.0,
    "Louisiana": 0.0,
    "Maine": 0.0,
    "Maryland": 0.0,
    "Massachusetts": 0.0,
    "Michigan": 0.0,
    "Minnesota": 0.0,
    "Mississippi": 0.0,
    "Missouri": 0.0,
    "Montana": 0.0,
    "Nebraska": 0.0,
    "Nevada": 0.0,
    "New Hampshire": 0.0,
    "New Jersey": 0.0,
    "New Mexico": 0.0,
    "New York": 0.0,
    "North Carolina": 0.0,
    "North Dakota": 0.0,
    "Ohio": 0.0,
    "Oklahoma": 0.0,
    "Oregon": 0.0,
    "Pennsylvania": 0.0,
    "Rhode Island": 0.0,
    "South Carolina": 0.0,
    "South Dakota": 0.0,
    "Tennessee": 0.0,
    "Texas":0.0,
    "Utah": 0.0,
    "Vermont": 0.0,
    "Virginia": 0.0,
    "Washington": 0.0,
    "West Virginia": 0.0,
    "Wisconsin": 0.0,
    "Wyoming": 0.0,
    "Washington, District of Columbia": 0.0 #District - Not a State
    }

    #if (len(row.delivery_by_region) > 1):

    for item in row.delivery_by_region:
        #try:
        if ((item['region'] == 'Unknown') | (item['percentage'] == 'Unknown')):
            pass
        else:
            # print(row.page_name)
            # print(row.delivery_by_region)
            # print("##############################################################")
            state = item['region']
            if "Columbia" in state:
                state = 'Washington, District of Columbia'
            elif state not in states:
                print(state)
                pass
            else:
            # print(state)
            # print(type(state))
                percentage = float(item['percentage'])
            # print(percentage)
            # print(type(percentage))
                states[state] += percentage
            # except:
        #     lst_of_failed.append(row[['page_name', 'delivery_by_region']])
        #     pass  

    # elif(len(row.delivery_by_region) == 1):
    #     #print(row)
    #     if ((row.delivery_by_region[0]['region'] != 'Unknown') & (row.delivery_by_region[0]['percentage'] != 'Unknown')):
    #         state = row.delivery_by_region[0]['region']
    #         percentage = float(row.delivery_by_region[0]['percentage'])
    #         states[state] = states.get(state) + percentage
        
    for key, value in states.items():
        states_lst.append(value*row['impressions_hi']) # CHANGED SOMETHING HERE NOT TESTED

    return pd.Series(states_lst)


   
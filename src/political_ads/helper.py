#Get gender distribution
def get_gender_distribution(lst):
    percentage = 0.0
    for item in lst:
        if item['gender'] == 'male':
            percentage += float(item['percentage'])
    return percentage

#Get age distribution
def get_age_distribution(lst, all_ages=False):
    age_dist = {}
    if all_ages == True:
        age_dist = {"13-17": 0.0, '18-24': 0.0, '25-34':0.0, '35-44':0.0, '45-54':0.0, '55-64':0.0, '65+':0.0}
    for item in lst:
        age = item['age']
        percentage = float(item['percentage'])
        if age_dist.get(age) == None:
            age_dist[age] = percentage
        else:
            age_dist[age] = age_dist.get(age) + percentage
    return age_dist


# This function returns the average of a range (for impressions and spend)
def transform_range(entry: dict):
    
    lower = entry["lower_bound"]
    if entry.get("upper_bound") == None:
        higher = entry["lower_bound"]
    else:
        higher = entry["upper_bound"]
    return int(int(lower) + int(higher)) / 2


# Transoforms spend and impressions back to dictionnaries when reading from csv
def string_to_dict(dict_string):
    import json 
    # Convert to proper json format
    dict_string = dict_string.replace("'", '"')
    return json.loads(dict_string)
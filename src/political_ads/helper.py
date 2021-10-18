#Get gender distribution
def get_gender_distribution(lst):
    percentage = 0.0
    for item in lst:
        if item['gender'] == 'male':
            percentage += float(item['percentage'])
    return percentage

#Get age distribution
def get_age_distribution(lst, all_ages):
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
    return int(int(entry["lower_bound"]) + int(entry["upper_bound"])) / 2
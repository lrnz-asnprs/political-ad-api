#Get gender distribution
def get_gender_distribution(lst):
    percentage = 0.0
    for item in lst:
        if item['gender'] == 'male':
            percentage += float(item['percentage'])
    return percentage

#Get age distribution
def get_age_distribution(lst):
    age_dist = {}
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
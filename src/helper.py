# This function returns the average of a range (for impressions and spend)
def transform_range(entry: dict):
    return int(int(entry["lower_bound"]) + int(entry["upper_bound"])) / 2
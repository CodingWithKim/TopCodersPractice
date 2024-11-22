country_info = {
    "Population" : {"Johor": 10000, "Melaka": 15000, "Kuala Lumpur": 300000},
    "Income" : {"Melaka": 5999, "Kuala Lumpur": 39999, "Penang": 29999},
    "Postcode": {"Penang": 85600, "Johor": 85000, "Kuala Lumpur": 43500}
}

def get_info(state_name):
    result = []
    for index, value in country_info.items():
        if state_name in value.keys():
            result.append((index, value.get(state_name)))
    return result


print(get_info("Johor"))
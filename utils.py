from collections import OrderedDict

def region(data):
    regiones = list(map(lambda x: x['region'], data))
    return list(OrderedDict.fromkeys(regiones))

def worldHappiness2022(data, region):
    filtered_data = list(filter(lambda item: item['region'] == region, data))
    countries = list(map(lambda x: x['country'], filtered_data))
    worldHappiness2022_values = list(map(lambda x: float(x['WorldHappiness2022']), filtered_data))
    return countries, worldHappiness2022_values

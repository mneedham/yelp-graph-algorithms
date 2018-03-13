import json

import reverse_geocoder as rg

lat_longs = {}

with open("dataset/business.json") as business_json:
    for line in business_json.readlines():
        item = json.loads(line)
        if item["latitude"] and item["longitude"]:
            lat_longs[item["business_id"]] = ((item["latitude"], item["longitude"]))

result = {}
for business_id, location in zip(list(lat_longs.keys()), rg.search(list(lat_longs.values()))):
    result[business_id] = {
        "country": location["cc"], "name": location["name"],
        "admin1": location["admin1"], "admin2": location["admin2"]
    }

with open("dataset/businessLocations.json", "w") as business_locations_json:
    json.dump(result, business_locations_json, indent=4, sort_keys=True)

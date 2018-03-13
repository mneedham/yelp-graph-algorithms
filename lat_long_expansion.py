import csv
import json

import reverse_geocoder as rg

# coordinates = (51.5214588, -0.1729636), (9.936033, 76.259952), (37.38605, -122.08385)
#
# results = rg.search(coordinates)  # default mode = 2
#
# print(results)

mapping = {}
# lat_longs = []
# count = 0

# with open("dataset/business.json") as business_json:
#     for line in business_json.readlines()[:10000]:
#         item = json.loads(line)
#
#         if item["latitude"] and item["longitude"]:
#             lat_longs.append((item["latitude"], item["longitude"]))
#             count += 1
#
#             if count % 10000 == 0:
#                 for row in rg.search(lat_longs):
#                     result[(row["lat"], row["lon"])] = {
#                         "country": row["cc"], "name": row["name"],
#                         "admin1": row["admin1"], "admin2": row["admin2"]
#                     }
#                 lat_longs = []

# print(result)
#
# with open("dataset/business.json") as business_json, \
#         open("dataset/businessLocations.json", "w") as business_locations_json:
#
#     for line in business_json.readlines()[:1000]:
#         item = json.loads(line)
#
#         row = result.get((item["latitude"], item["longitude"]))
#         if row:
#             print(item, row)


# too slow
# with open("dataset/business.json") as business_json, \
#     open("dataset/businessLocations.json") as business_locations_json:
#     for line in business_json.readlines()[:10000]:
#         item = json.loads(line)
#
#         if item["latitude"] and item["longitude"]:
#             for row in rg.search((item["latitude"], item["longitude"])):
#                 mapping[item["business_id"]] = {
#                     "country": row["cc"], "name": row["name"],
#                     "admin1": row["admin1"], "admin2": row["admin2"]
#                 }
#
#     json.dump(mapping, business_locations_json)



# for lat_long in lat_longs:
#     print(lat_long)
#
# output = {}
# with open("dataset/lat_longs.json", "w") as lat_longs_json:
#     for row in rg.search(lat_longs):
#         print(row)
#         output["{0},{1}".format(row["lat"], row["lon"])] = {
#             "country": row["cc"],
#             "name": row["name"],
#             "admin1": row["admin1"],
#             "admin2": row["admin2"]
#         }
#
#     json.dump(output, lat_longs_json)

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
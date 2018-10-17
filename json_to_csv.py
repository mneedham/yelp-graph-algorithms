import csv
import json
import os


def write_header(file_name, columns):
    with open(file_name, 'w') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(columns)

source_dir = "dataset-round12"
destination_dir = "data-round12"

if not os.path.isfile(f"{destination_dir}/business_header.csv"):
    with open(f"{source_dir}/yelp_academic_dataset_business.json") as business_json, \
         open(f"{destination_dir}/business.csv", 'w') as business_csv:

        write_header(f"{destination_dir}/business_header.csv",
                     ['id:ID(Business)', 'name', 'address', 'city', 'state', 'location:Point(WGS-84)'])

        business_writer = csv.writer(business_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in business_json.readlines():
            item = json.loads(line)
            try:
                point = ""
                if "latitude" in item and "longitude" in item:
                    if item["latitude"] and item["longitude"]:
                        point = "{latitude: %s, longitude: %s}" % (item["latitude"], item["longitude"])

                business_writer.writerow([item['business_id'], item['name'], item['address'], item['city'], item['state'], point])
            except Exception as e:
                print(item)
                raise e

if not os.path.isfile(f"{destination_dir}/city_header.csv"):
    with open(f"{source_dir}/yelp_academic_dataset_business.json") as business_json, \
            open(f"{destination_dir}/city.csv", "w") as city_csv, \
            open(f"{destination_dir}/business_IN_CITY_city.csv", "w") as business_city_csv:

        write_header(f"{destination_dir}/city_header.csv", ['name:ID(City)'])
        write_header(f"{destination_dir}/business_IN_CITY_city_header.csv", [':START_ID(Business)', ':END_ID(City)'])

        business_city_writer = csv.writer(business_city_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        city_writer = csv.writer(city_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_cities = set()
        for line in business_json.readlines():
            item = json.loads(line)

            if item["city"].strip():
                unique_cities.add(item["city"])
                business_city_writer.writerow([item["business_id"], item["city"]])

        for city in unique_cities:
            city_writer.writerow([city])

if not os.path.isfile(f"{destination_dir}/area_header.csv"):
    with open(f"{source_dir}/businessLocations.json") as business_locations_json, \
            open(f"{destination_dir}/area.csv", "w") as area_csv, \
            open(f"{destination_dir}/country.csv", "w") as country_csv, \
            open(f"{destination_dir}/city_IN_AREA_area.csv", "w") as city_area_csv, \
            open(f"{destination_dir}/area_IN_COUNTRY_country.csv", "w") as area_country_csv:
        input = json.load(business_locations_json)

        write_header(f"{destination_dir}/area_header.csv", ['name:ID(Area)'])
        write_header(f"{destination_dir}/country_header.csv", ['name:ID(Country)'])

        write_header(f"{destination_dir}/city_IN_AREA_area_header.csv", [':START_ID(City)', ':END_ID(Area)'])
        write_header(f"{destination_dir}/area_IN_COUNTRY_country_header.csv", [':START_ID(Area)', ':END_ID(Country)'])

        area_writer = csv.writer(area_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        country_writer = csv.writer(country_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        city_area_writer = csv.writer(city_area_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        area_country_writer = csv.writer(area_country_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_areas = set()
        unique_countries = set()
        unique_city_areas = set()
        unique_area_countries = set()

        for business_id in input:
            if input[business_id]["admin1"]:
                unique_areas.add(input[business_id]["admin1"])
                unique_countries.add(input[business_id]["country"])

                unique_city_areas.add((input[business_id]["city"], input[business_id]["admin1"]))
                unique_area_countries.add((input[business_id]["admin1"], input[business_id]["country"]))

        for area in unique_areas:
            area_writer.writerow([area])

        for country in unique_countries:
            country_writer.writerow([country])

        for city, area in unique_city_areas:
            city_area_writer.writerow([city, area])

        for area, country in unique_area_countries:
            area_country_writer.writerow([area, country])

if not os.path.isfile(f"{destination_dir}/category_header.csv"):
    with open(f"{source_dir}/yelp_academic_dataset_business.json") as business_json, \
            open(f"{destination_dir}/category.csv", 'w') as categories_csv, \
            open(f"{destination_dir}/business_IN_CATEGORY_category.csv", 'w') as business_category_csv:

        write_header(f"{destination_dir}/category_header.csv", ['name:ID(Category)'])
        write_header(f"{destination_dir}/business_IN_CATEGORY_category_header.csv", [':START_ID(Business)', ':END_ID(Category)'])

        business_category_writer = csv.writer(business_category_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        category_writer = csv.writer(categories_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_cities = set()
        for line in business_json.readlines():
            item = json.loads(line)
            if item["categories"]:
                for category in item["categories"].split(","):
                    category = category.strip()
                    unique_cities.add(category)
                    business_category_writer.writerow([item["business_id"], category])

        for category in unique_cities:
            try:
                category_writer.writerow([category])
            except Exception as e:
                print(category)
                raise e

if not os.path.isfile(f"{destination_dir}/user_header.csv"):
    with open(f"{source_dir}/yelp_academic_dataset_user.json") as user_json, \
            open(f"{destination_dir}/user.csv", 'w') as user_csv, \
            open(f"{destination_dir}/user_FRIENDS_user.csv", 'w') as user_user_csv:

        write_header(f"{destination_dir}/user_header.csv", ['id:ID(User)', 'name'])
        write_header(f"{destination_dir}/user_FRIENDS_user_header.csv", [':START_ID(User)', ':END_ID(User)'])

        user_writer = csv.writer(user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        user_user_writer = csv.writer(user_user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in user_json.readlines():
            item = json.loads(line)
            user_writer.writerow([item["user_id"], item["name"]])
            if item["friends"] != "None":
                for friend_id in item["friends"].split(","):
                    friend_id = friend_id.strip()
                    user_user_writer.writerow([item["user_id"], friend_id])

if not os.path.isfile(f"{destination_dir}/review_header.csv"):
    with open(f"{source_dir}/yelp_academic_dataset_review.json") as review_json, \
            open(f"{destination_dir}/review.csv", 'w') as review_csv, \
            open(f"{destination_dir}/user_WROTE_review.csv", 'w') as user_review_csv, \
            open(f"{destination_dir}/review_REVIEWS_business.csv", 'w') as review_business_csv:

        write_header(f"{destination_dir}/review_header.csv", ['id:ID(Review)', 'text', 'stars:int', 'date'])
        write_header(f"{destination_dir}/user_WROTE_review_header.csv", [':START_ID(User)', ':END_ID(Review)'])
        write_header(f"{destination_dir}/review_REVIEWS_business_header.csv", [':START_ID(Review)', ':END_ID(Business)'])

        review_writer = csv.writer(review_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        user_review_writer = csv.writer(user_review_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        review_business_writer = csv.writer(review_business_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in review_json.readlines():
            item = json.loads(line)
            review_writer.writerow([item["review_id"], item["text"], item["stars"], item["date"]])
            user_review_writer.writerow([item["user_id"], item["review_id"]])
            review_business_writer.writerow([item["review_id"], item["business_id"]])

if not os.path.isfile(f"{destination_dir}/photo_header.csv"):
    with open(f"{source_dir}/yelp_academic_dataset_photo_features.csv") as photo_features_csv, \
         open(f"{source_dir}/yelp_academic_dataset_photo.json") as photo_json, \
         open(f"{destination_dir}/photo.csv", "w") as photo_csv:

        write_header(f"{destination_dir}/photo_header.csv",
                     ['id:ID(Photo)', 'embedding', 'caption', 'label'])

        photo_writer = csv.writer(photo_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        photos = {}
        for line in photo_json.readlines():
            item = json.loads(line)
            photos[item["photo_id"]] = {
                "business_id": item["business_id"],
                "caption": item["caption"],
                "label": item["label"]
            }

        photo_csv_reader = csv.reader(photo_features_csv, delimiter=",")
        next(photo_csv_reader)
        for row in photo_csv_reader:
            photo_id = row[0]
            embedding = row[1:]
            photo_details = photos[photo_id]
            # print(photo_id, embedding, photo_details)
            photo_writer.writerow([photo_id,
                                   embedding,
                                   photo_details["caption"],
                                   photo_details["label"]])
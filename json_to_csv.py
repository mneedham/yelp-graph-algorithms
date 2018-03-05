import csv
import json
import os


def write_header(file_name, columns):
    with open(file_name, 'w') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(columns)


if not os.path.isfile("data/business.csv"):
    with open("dataset/business.json") as business_json, \
            open("data/business.csv", 'w') as business_csv, \
            open("data/business_header.csv", 'w') as business_header_csv:

        write_header(business_header_csv, ['id:ID(Business)', 'name', 'address', 'city', 'state'])

        business_writer = csv.writer(business_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in business_json.readlines():
            item = json.loads(line)
            try:
                business_writer.writerow([item['business_id'], item['name'], item['address'], item['city'], item['state']])
            except Exception as e:
                print(item)
                raise e

if not os.path.isfile("data/categories.csv"):
    with open("dataset/business.json") as business_json, \
            open("data/category.csv", 'w') as categories_csv, \
            open("data/business_IN_CATEGORY_category.csv", 'w') as categories_business_csv:

        write_header("data/category_header.csv", ['name:ID(Category)'])
        write_header("data/business_IN_CATEGORY_category_header.csv", [':START_ID(Business)', ':END_ID(Category)'])

        categories_businesses_writer = csv.writer(categories_business_csv, escapechar='\\', quotechar='"',
                                                  quoting=csv.QUOTE_ALL)
        category_writer = csv.writer(categories_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_categories = set()
        for line in business_json.readlines():
            item = json.loads(line)
            for category in item["categories"]:
                unique_categories.add(category)
                categories_businesses_writer.writerow([item["business_id"], category])

        for category in unique_categories:
            try:
                category_writer.writerow([category])
            except Exception as e:
                print(category)
                raise e

if not os.path.isfile("data/user.csv"):
    with open("dataset/user.json") as user_json, \
            open("data/user.csv", 'w') as user_csv, \
            open("data/user_FRIENDS_user.csv", 'w') as user_user_csv:

        write_header("data/user_header.csv", ['id:ID(User)', 'name'])
        write_header("data/user_FRIENDS_user_header.csv", [':START_ID(User)', ':END_ID(User)'])

        user_writer = csv.writer(user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        user_user_writer = csv.writer(user_user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in user_json.readlines():
            item = json.loads(line)
            user_writer.writerow([item["user_id"], item["name"]])
            for friend_id in item["friends"]:
                user_user_writer.writerow([item["user_id"], friend_id])

if not os.path.isfile("data/review.csv"):
    with open("dataset/review.json") as review_json, \
            open("data/review.csv", 'w') as review_csv, \
            open("data/user_WROTE_review.csv", 'w') as user_review_csv, \
            open("data/review_REVIEWS_business.csv", 'w') as review_business_csv:

        write_header("data/review_header.csv", ['id:ID(Review)', 'text', 'stars:int', 'date'])
        write_header("data/user_WROTE_review_header.csv", [':START_ID(User)', ':END_ID(Review)'])
        write_header("data/review_REVIEWS_business_header.csv", [':START_ID(Review)', ':END_ID(Business)'])

        review_writer = csv.writer(review_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        user_review_writer = csv.writer(user_review_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        review_business_writer = csv.writer(review_business_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in review_json.readlines():
            item = json.loads(line)
            review_writer.writerow([item["review_id"], item["text"], item["stars"], item["date"]])
            user_review_writer.writerow([item["user_id"], item["review_id"]])
            review_business_writer.writerow([item["review_id"], item["business_id"]])

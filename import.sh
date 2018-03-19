#!/usr/bin/env bash

export DATA=/Users/markneedham/projects/yelp-graph-algorithms/data/

./bin/neo4j-admin import \
    --mode=csv \
    --database=yelp.db \
    --nodes:Business $DATA/business_header.csv,$DATA/business.csv \
    --nodes:Category $DATA/category_header.csv,$DATA/category.csv \
    --nodes:User $DATA/user_header.csv,$DATA/user.csv \
    --nodes:Review $DATA/review_header.csv,$DATA/review.csv \
    --nodes:City $DATA/city_header.csv,$DATA/city.csv \
    --nodes:Area $DATA/area_header.csv,$DATA/area.csv \
    --nodes:Country $DATA/country_header.csv,$DATA/country.csv \
    --relationships:IN_CATEGORY $DATA/business_IN_CATEGORY_category_header.csv,$DATA/business_IN_CATEGORY_category.csv \
    --relationships:FRIENDS $DATA/user_FRIENDS_user_header.csv,$DATA/user_FRIENDS_user.csv \
    --relationships:WROTE $DATA/user_WROTE_review_header.csv,$DATA/user_WROTE_review.csv \
    --relationships:REVIEWS $DATA/review_REVIEWS_business_header.csv,$DATA/review_REVIEWS_business.csv \
    --relationships:IN_CITY $DATA/business_IN_CITY_city_header.csv,$DATA/business_IN_CITY_city.csv \
    --relationships:IN_AREA $DATA/city_IN_AREA_area_header.csv,$DATA/city_IN_AREA_area.csv \
    --relationships:IN_COUNTRY $DATA/area_IN_COUNTRY_country_header.csv,$DATA/area_IN_COUNTRY_country.csv \
    --ignore-missing-nodes=true \
    --multiline-fields=true



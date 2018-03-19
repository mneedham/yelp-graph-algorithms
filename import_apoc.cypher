// Create businesses and categories
CALL apoc.load.json('file:///Users/markneedham/projects/yelp-graph-algorithms/dataset/business.json')
YIELD value
WITH value LIMIT 1000
MERGE (b:Business {id:value.business_id})
SET b += apoc.map.clean(value, ['attributes','hours','business_id','categories','address','postal_code'], [])
WITH b,value.categories as categories
UNWIND categories as category
MERGE (c:Category{name:category})
MERGE (b)-[:IN_CATEGORY]->(c);

CALL apoc.load.json('file:///Users/markneedham/projects/yelp-graph-algorithms/dataset/user.json')
YIELD value
WITH value LIMIT 1000
MERGE (u:User {id:value.user_id})
SET u += apoc.map.clean(value, ['friends','user_id'], [])
WITH u, value.friends as friends
UNWIND friends as friend
MERGE (u1:User {id:friend})
MERGE (u)-[:FRIENDS]-(u1);


CALL apoc.load.json('file:///Users/markneedham/projects/yelp-graph-algorithms/dataset/review.json')
YIELD value
WITH value LIMIT 50000
MERGE (b:Business {id:value.business_id})
MERGE (u:User {id:value.user_id})
MERGE (r:Review {id:value.review_id})
MERGE (u)-[:WROTE]->(r)
MERGE (r)-[:REVIEWS]->(b)
SET r += apoc.map.clean(value, ['business_id','user_id','review_id'], []);





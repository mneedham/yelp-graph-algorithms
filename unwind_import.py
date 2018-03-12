import json

from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo"))

with open("dataset/business.json", 'r') as file:
    with driver.session() as session:
        count = 0
        items = []
        for line in file.readlines()[:2000]:
            item = json.loads(line)
            items.append(item)
            count += 1
            if count >= 1000:
                session.run('''
                    WITH {businesses} AS businesses
                    UNWIND businesses AS business
                    MERGE (b:Business {id: business.business_id})
                    SET b.name = business.name,
                        b.city = business.city
                    WITH *
                    UNWIND business.categories AS cat
                    MERGE (c:Category {name: cat})
                    MERGE (b)-[:IN_CATEGORY]->(c)
                ''', parameters={'businesses': items}).consume()
                count = 0

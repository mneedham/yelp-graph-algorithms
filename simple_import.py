from neo4j.v1 import GraphDatabase
import json

driver = GraphDatabase.driver("bolt://localhost", auth=("neo4j", "neo"))

with open("dataset/business.json", 'r') as file:
    with driver.session() as session:
        for line in file.readlines()[:10]:
            item = json.loads(line)
            print(item)

            session.run('''
                WITH {business} AS business
                MERGE (b:Business {id: business.business_id})
                SET b.name = business.name,
                    b.city = business.city
                WITH *
                UNWIND business.categories AS cat
                MERGE (c:Category {name: cat})
                MERGE (b)-[:IN_CATEGORY]->(c)
            ''', parameters={'business': item}).consume()

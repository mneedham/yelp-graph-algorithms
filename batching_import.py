from neo4j.v1 import GraphDatabase
import json

driver = GraphDatabase.driver("bolt://localhost", auth=("neo4j", "neo"))

with open("dataset/business.json", 'r') as file:
    with driver.session() as session:
        count = 0
        tx = session.begin_transaction()
        for line in file.readlines()[:2000]:
            item = json.loads(line)
            tx.run('''
                WITH {business} AS business
                MERGE (b:Business {id: business.business_id})
                SET b.name = business.name,
                    b.city = business.city
                WITH *
                UNWIND business.categories AS cat
                MERGE (c:Category {name: cat})
                MERGE (b)-[:IN_CATEGORY]->(c)
            ''', parameters={'business': item})
            count += 1
            if count > 1000:
                tx.commit()
                tx = session.begin_transaction()
                count = 0
        tx.commit()

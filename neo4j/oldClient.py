import sys
from neo4j import GraphDatabase

# Initiate connection to neo4j
uri = "bolt://10.10.1.201:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "1234"))

# Read queries
file = open("Queries.txt", "r")
data = file.read()
queries = data.split("-------------------------------------")

# Run query
with driver.session() as session:
    result = session.run(queries[int(sys.argv[1]) - 1])

# Print result
records = result.records()

for i in records:
    print(i)

#!/usr/bin/env python3

import os
import re
import sys
import yaml
import psycopg2


# Initiate connection to postgres
conn = psycopg2.connect("dbname=ldbcsf1 user=postgres")
cur = conn.cursor()


# Read queries
queries = []
with open(os.path.dirname(__file__) + '/Queries.yaml') as f:
    queries = yaml.load(f, Loader=yaml.FullLoader)["queries"]


def replaceParams(query):
    for key, value in query["params"].items():
        query["sql"] = query["sql"].replace(':' + key, str(value))
    return query


queries = list(map(lambda q: replaceParams(q), queries))

# Run query
# idx = int(sys.argv[1]) - 1
f = open("queries", "w")
for idx in range(5):
    print(queries[idx]["name"])
    f.write(queries[idx]["name"] + "\n")
    f.write(queries[idx]["sql"] + "\n\n")
    try:
        cur.execute(queries[idx]["sql"])
        # Print result
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Exception as E:
        print(E)
        conn.rollback()
    print()
    

# Make the changes to the database persistent
# conn.commit()

# Close communication with the database
cur.close()
conn.close()

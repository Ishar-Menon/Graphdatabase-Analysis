#!/usr/bin/env python3

import os
import re
import yaml
import argparse
import psycopg2

parser = argparse.ArgumentParser(
    description='Run a single query chosen from Queries.yaml')
parser.add_argument(
    "index", help="index of the query to execute (1-based index)", type=int)
args = parser.parse_args()


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

# Execute query
idx = args.index - 1
cur.execute(queries[idx]["sql"])

# Print results
try:
    rows = cur.fetchall()
    for row in rows:
        print(row)
except psycopg2.ProgrammingError:
    print("no results to fetch")

# # Make the changes to the database persistent
# conn.commit()

# Close communication with the database
cur.close()
conn.close()

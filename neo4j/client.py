import sys
from neo4j import GraphDatabase
import time
import threading

# Initiate connection to neo4j
uri = "bolt://10.10.1.201:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "1234"))

# Read queries
file = open("Queries.txt", "r")
data = file.read()
queries = data.split("-------------------------------------")


def queryDB():
    global driver
    global queries
    with driver.session() as session:
        result = session.run(queries[int(sys.argv[1]) - 1])

    # Print result
    records = result.records()

    for i in records:
        print(i)


if(int(sys.argv[1]) != 4):

    Threads = []

    for i in range(100):
        Threads.append(threading.Thread(target=queryDB))

    for i in range(5):
        for j in range(20):
            Threads[20*i + j].start()
        time.sleep(5)

    for i in range(100):
        Threads[i].join()
else:
    Threads = []

    for i in range(20):
        Threads.append(threading.Thread(target=queryDB))

    for i in range(0, 20, 4):
        Threads[i].start()
        Threads[i+1].start()
        Threads[i+2].start()
        Threads[i+3].start()
        time.sleep(5)

    for i in range(20):
        Threads[i].join()

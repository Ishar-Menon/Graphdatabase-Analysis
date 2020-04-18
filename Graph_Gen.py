import numpy as np
import matplotlib.pyplot as plt
import csv

postgres_path = 'D:\\College\\PES\\Semester-6\\Cloud - Computing\\Graphdatabase-Analysis\\postgres\Data\\'
neo4j_path = 'D:\\College\\PES\\Semester-6\\Cloud - Computing\\Graphdatabase-Analysis\\neo4j\Data\\'

y_neo4j = []
y_postgress = []
x_common = ['Trial 1','Trial 2','Trial 3','Trial 4','Trial 5']

options = ['Cache_References','Instruction_Count']
postgress_fname = postgres_path + options[1] + '.csv'
neo4j_fname = neo4j_path + options[1] + '.csv'

with open(postgress_fname) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')
    for row in csv_reader:
        if (row[6] == 'Average'):
            continue
        else:
            y_postgress.append(float(row[6]))

with open(neo4j_fname) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')
    for row in csv_reader:
        if (row[6] == 'Average'):
            continue
        else:
            y_neo4j.append(float(row[6]))

#print(y_postgress)
#print(y_neo4j)
plt.plot(x_common,y_neo4j,label = 'Neo4j')
plt.plot(x_common,y_postgress,label = 'postgress')
plt.xlabel('Trials')
plt.ylabel(options[1])
plt.title('Neo4j - Postgres Combined - ' + options[1])
plt.legend()
plt.show()

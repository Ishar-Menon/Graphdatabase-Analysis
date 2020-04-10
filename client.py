from neo4j import GraphDatabase

uri = "bolt://10.10.1.201:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "1234"))

with driver.session() as session:
    result = session.run("""MATCH (:Person {id:1129})<-[:HAS_CREATOR]-(m:Message)-[:REPLY_OF*0..]->(p:Post) MATCH (p)-[:HAS_CREATOR]->(c)RETURN                                                                                                            
  m.id as messageId,                                                                                                
  CASE exists(m.content)                                                                                            
  WHEN true THEN m.content                                                                                          
  ELSE m.imageFile                                                                                                  
  END AS messageContent,
  m.creationDate AS messageCreationDate,                                                                            
  p.id AS originalPostId,                                                                                           
  c.id AS originalPostAuthorId,
  c.firstName as originalPostAuthorFirstName,                                                                       
  c.lastName as originalPostAuthorLastName                                                                          
  ORDER BY messageCreationDate DESC""")

print(result.records())

records = result.records()
keys = result.keys()

for i in records:
    print(i)
    print()
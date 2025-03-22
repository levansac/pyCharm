from cassandra.cluster import Cluster
from uuid import uuid4

# Connect to Cassandra cluster
cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra node IP or hostname
session = cluster.connect('cassandrakeyspace')  # Replace with your keyspace name

# Insert 10,000 records
for i in range(1, 10001):
    session.execute(
        """
        INSERT INTO ROLE (Id, RoleCode, RoleName, Descriptions)
        VALUES (%s, %s, %s, %s)
        """,
        (uuid4(), f'D{i}', f'Role {i}', f'Description for role {i}')
    )

print("Inserted 10,000 records.")

from cassandra.cluster import Cluster
from uuid import uuid4
from datetime import datetime

def insert_roles(record_count=1000):
    # Connect to Cassandra
    cluster = Cluster(['127.0.0.1'])  # Replace with your IP/hostname
    session = cluster.connect('cassandrakeyspace')  # Replace with your keyspace

    # Prepare the insert statement
    insert_stmt = session.prepare("""
        INSERT INTO ROLE (Id, RoleCode, RoleName, Status, Descriptions, CreatedDate, ModifiedDate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """)

    for i in range(1, record_count + 1):
        now = datetime.now()

        session.execute(insert_stmt, (
            uuid4(),
            f'ROLE{i}',
            f'Role {i}',
            1,
            f'Description for role {i}',
            now,
            now
        ))

        if i % 1000 == 0:
            print(f'{i} records inserted...')

    print(f"Inserted {record_count} records successfully.")

if __name__ == "__main__":
    insert_roles(1000)  # You can change this number

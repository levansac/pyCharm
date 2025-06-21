import uuid
import random
from datetime import datetime
from cassandra.cluster import Cluster
from faker import Faker

# Setup
KEYSPACE = 'cassandrakeyspace'  # Replace with your keyspace name
EMPLOYEE_TABLE = 'employee'
DEPARTMENT_TABLE = 'department'
ROLE_TABLE = 'role'

cluster = Cluster(['127.0.0.1'])  # Update host if needed
session = cluster.connect(KEYSPACE)

fake = Faker()

# Step 1: Fetch DepartmentId for DepartmentName = 'IT'
query_dept = f"SELECT Id FROM department WHERE DepartmentCode = 'IT' ALLOW FILTERING"
row_dept = session.execute(query_dept).one()
department_id = row_dept.id  # Use this for all employees

# Step 2: Use fixed RoleId
query_role = f"SELECT Id FROM role WHERE RoleCode = 'DEV' ALLOW FILTERING"
row_role = session.execute(query_role).one()
role_id = row_role.id  # Use this for all employees

# Step 3: Prepare insert query
insert_query = session.prepare(f'''
INSERT INTO {EMPLOYEE_TABLE} (
    Id, EmployeeCode, FirstName, LastName, Email, Phone,
    DepartmentId, RoleId, Status, StartDate, EndDate,
    CreatedDate, ModifiedDate
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''')

# Step 4: Insert 1000 fake employees
for _ in range(3000):
    emp_id = uuid.uuid4()
    emp_code = f"EMP{random.randint(10000, 99999)}"
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    status = random.choice([0, 1])
    start_date = fake.date_time_between(start_date='-5y', end_date='-1d')
    end_date = None if status == 1 else fake.date_time_between(start_date=start_date, end_date='now')
    created_date = datetime.now()
    modified_date = datetime.now()

    session.execute(insert_query, (
        emp_id, emp_code, first_name, last_name, email, phone,
        department_id, role_id, status,
        start_date, end_date, created_date, modified_date
    ))

print("✅ Successfully inserted 1000 employees into the IT department.")

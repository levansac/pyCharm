CREATE TABLE employee (
    Id UUID PRIMARY KEY,
    EmployeeCode TEXT,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    Phone TEXT,
    DepartmentId UUID,  -- Reference to department table
    RoleId UUID,        -- Reference to role table
    CreatedDate TIMESTAMP,
    ModifiedDate TIMESTAMP
);
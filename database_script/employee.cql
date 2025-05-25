CREATE TABLE employee (
    Id UUID PRIMARY KEY,
    EmployeeCode TEXT,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    Phone TEXT,
    DepartmentId UUID,  -- Reference to department table
    RoleId UUID,        -- Reference to role table
    Status TINYINT,
    StartDate TIMESTAMP,
    EndDate TIMESTAMP,
    CreatedDate TIMESTAMP,
    ModifiedDate TIMESTAMP
);

--This allows you to query EmployeeCode without requiring ALLOW FILTERING
CREATE INDEX employee_code_idx ON employee (EmployeeCode);
CREATE INDEX employee_firstname_idx ON employee (FirstName);

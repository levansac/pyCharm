CREATE TABLE employee (
    Id UUID PRIMARY KEY,
    EmployeeCode TEXT,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    Phone TEXT,
    DepartmentId UUID,  -- Reference to department table
    RoleId UUID,        -- Reference to role table
    StartDate TIMESTAMP,
    EndDate TIMESTAMP,
    CreatedDate TIMESTAMP,
    ModifiedDate TIMESTAMP
);

--This allows you to query EmployeeCode without requiring ALLOW FILTERING
CREATE INDEX employee_code_idx ON employee (EmployeeCode);
CREATE INDEX employee_firstname_idx ON employee (FirstName);

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP001', 'John', 'Doe', 'john.doe@example.com', '+1234567890', uuid(), uuid(), toTimestamp(now()), null, toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP002', 'Jane', 'Smith', 'jane.smith@example.com', '+1987654321', uuid(), uuid(), toTimestamp(now()), null, toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP003', 'Alice', 'Johnson', 'alice.johnson@example.com', '+1122334455', uuid(), uuid(), toTimestamp(now()), null, toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP004', 'Bob', 'Williams', 'bob.williams@example.com', '+1223344556', uuid(), uuid(), toTimestamp(now()), null, toTimestamp(now()), toTimestamp(now()));

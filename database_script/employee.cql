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

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP001', 'John', 'Doe', 'john.doe@example.com', '+1234567890', uuid(), uuid(), 1, '2022-01-10', null, toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP002', 'Alice', 'Smith', 'alice.smith@example.com', '+1987654321', uuid(), uuid(), 0, '2021-05-15', '2023-12-31', toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP003', 'Michael', 'Brown', 'michael.brown@example.com', '+1122334455', uuid(), uuid(), 1, '2023-06-20', null, toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP004', 'Emily', 'Johnson', 'emily.johnson@example.com', '+1223344556', uuid(), uuid(), 1, '2020-09-25', null, toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP005', 'Robert', 'Wilson', 'robert.wilson@example.com', '+1555666777', uuid(), uuid(), 0, '2018-03-12', '2022-06-30', toTimestamp(now()), toTimestamp(now()));

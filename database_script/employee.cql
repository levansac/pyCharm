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

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP001', 'John', 'Doe', 'john.doe@example.com', '+1234567890', e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 1, toTimestamp(now()), toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP002', 'Jane', 'Smith', 'jane.smith@example.com', '+0987654321', e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 1, toTimestamp(now()), toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP003', 'Michael', 'Brown', 'michael.brown@example.com', '+1122334455', e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 1, toTimestamp(now()), toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP004', 'Emily', 'Davis', 'emily.davis@example.com', '+5566778899', e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 1, toTimestamp(now()), toTimestamp(now()), toTimestamp(now()));

INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, CreatedDate, ModifiedDate)
VALUES (uuid(), 'EMP005', 'Daniel', 'Wilson', 'daniel.wilson@example.com', '+6677889900', e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 1, toTimestamp(now()), toTimestamp(now()), toTimestamp(now()));

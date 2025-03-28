CREATE TABLE history (
    Id UUID PRIMARY KEY,
    Action TEXT,
    ActionDate TIMESTAMP,
    EmployeeCode TEXT,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    Phone TEXT,
    DepartmentId UUID,  -- Reference to department table
    RoleId UUID,        -- Reference to role table
    Status TINYINT,
    StartDate TIMESTAMP,
    EndDate TIMESTAMP
);

--This allows you to query EmployeeCode without requiring ALLOW FILTERING
CREATE INDEX history_code_idx ON history (EmployeeCode);
CREATE INDEX history_firstname_idx ON history (FirstName);



INSERT INTO history (Id, EmployeeCode, Action, ActionDate, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate)
VALUES (uuid(), 'EMP001', 'Created', toTimestamp(now()), 'John', 'Doe', 'john.doe@example.com', '+1234567890',
        e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 1, '2024-01-01', NULL);

INSERT INTO history (Id, EmployeeCode, Action, ActionDate, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate)
VALUES (uuid(), 'EMP002', 'Updated', toTimestamp(now()), 'Jane', 'Smith', 'jane.smith@example.com', '+0987654321',
        e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 1, '2023-06-15', '2024-03-01');

INSERT INTO history (Id, EmployeeCode, Action, ActionDate, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate)
VALUES (uuid(), 'EMP003', 'Deleted', toTimestamp(now()), 'Alice', 'Brown', 'alice.brown@example.com', '+1122334455',
        e976253b-e5c8-43a7-bccb-07a788ad6d2a, f0f55a41-864b-4c7c-a217-43813c6c5db9, 0, '2022-11-10', '2023-12-31');

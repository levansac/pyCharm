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




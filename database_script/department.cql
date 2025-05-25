CREATE TABLE department (
    Id UUID PRIMARY KEY,
    DepartmentCode TEXT,
    DepartmentName TEXT,
    Status TINYINT,
    Descriptions TEXT,
    CreatedDate TIMESTAMP,
    ModifiedDate TIMESTAMP
);

--This allows you to query DepartmentCode without requiring ALLOW FILTERING
CREATE INDEX IF NOT EXISTS idx_departmentcode ON department (DepartmentCode);
CREATE INDEX IF NOT EXISTS idx_departmentname ON department (DepartmentName);
CREATE INDEX IF NOT EXISTS idx_status ON department (Status);

--This is script to insert data into DEPARTMENT table:
INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'HR', 'Human Resources', 'Handles employee records and hiring', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'IT', 'Information Technology', 'Manages company IT infrastructure', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'FIN', 'Finance', 'Handles company finances and budgeting', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'MKT', 'Marketing', 'Handles advertising and promotions', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'SALES', 'Sales', 'Manages client relationships and revenue', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'R&D', 'Research and Development', 'Develops new products and innovations', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'OPS', 'Operations', 'Ensures smooth daily business processes', 0, toTimestamp(now()), toTimestamp(now()));

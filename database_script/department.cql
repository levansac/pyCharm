CREATE TABLE department (
    Id UUID PRIMARY KEY,
    DepartmentCode TEXT,
    DepartmentName TEXT,
    Descriptions TEXT,
    CreatedDate TIMESTAMP,
    ModifiedDate TIMESTAMP,
);

--This allows you to query DepartmentCode without requiring ALLOW FILTERING
CREATE INDEX department_code_idx ON department (DepartmentCode);

--This is script to insert data into DEPARTMENT table:
INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'HR', 'Human Resources', 'Handles employee records and hiring', toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'IT', 'Information Technology', 'Manages company IT infrastructure', toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'FIN', 'Finance', 'Handles company finances and budgeting', toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'MKT', 'Marketing', 'Handles advertising and promotions', toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'SALES', 'Sales', 'Manages client relationships and revenue', toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'R&D', 'Research and Development', 'Develops new products and innovations', toTimestamp(now()), toTimestamp(now()));

INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'OPS', 'Operations', 'Ensures smooth daily business processes', toTimestamp(now()), toTimestamp(now()));




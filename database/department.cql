--This is creating key space
CREATE TABLE department (
    Id UUID PRIMARY KEY,
    DepartmentCode TEXT,
    DepartmentName TEXT,
    Descriptions TEXT
);


--This allows you to query DepartmentCode without requiring ALLOW FILTERING
CREATE INDEX department_code_idx ON department (DepartmentCode);

--This is script to insert data into DEPARTMENT table:
INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D001', 'Engineering', 'Responsible for developing and maintaining software.');

INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D002', 'Marketing', 'Handles advertising, promotions, and public relations.');

INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D003', 'Human Resources', 'Manages recruitment, employee relations, and payroll.');

INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D004', 'Sales', 'Responsible for selling products and services to clients.');


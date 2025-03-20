--This is creating key space
CREATE TABLE DEPARTMENT (
    Id UUID PRIMARY KEY,                -- Unique identifier for the department
    DepartmentCode TEXT,    -- DepartmentCode will also be part of the partition key
    DepartmentName TEXT,    -- Name of the department
    Descriptions TEXT,      -- Descriptions of the department
);
--This is script to insert data into DEPARTMENT table:
INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D001', 'Engineering', 'Responsible for developing and maintaining software.');

INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D002', 'Marketing', 'Handles advertising, promotions, and public relations.');

INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D003', 'Human Resources', 'Manages recruitment, employee relations, and payroll.');

INSERT INTO DEPARTMENT (Id, DepartmentCode, DepartmentName, Descriptions)
VALUES (uuid(), 'D004', 'Sales', 'Responsible for selling products and services to clients.');


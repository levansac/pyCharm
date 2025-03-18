--This is creating key space
CREATE TABLE DEPARTMENT (
    Id UUID PRIMARY KEY,
    DepartmentId TEXT,
    DepartmentName TEXT,
    Descriptions TEXT
);
--This is script to insert data into DEPARTMENT table:
INSERT INTO DEPARTMENT (Id, DepartmentId, DepartmentName, Descriptions)
VALUES (uuid(), 'D001', 'Engineering', 'Responsible for developing and maintaining software.');

INSERT INTO DEPARTMENT (Id, DepartmentId, DepartmentName, Descriptions)
VALUES (uuid(), 'D002', 'Marketing', 'Handles advertising, promotions, and public relations.');

INSERT INTO DEPARTMENT (Id, DepartmentId, DepartmentName, Descriptions)
VALUES (uuid(), 'D003', 'Human Resources', 'Manages recruitment, employee relations, and payroll.');

INSERT INTO DEPARTMENT (Id, DepartmentId, DepartmentName, Descriptions)
VALUES (uuid(), 'D004', 'Sales', 'Responsible for selling products and services to clients.');


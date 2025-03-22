CREATE TABLE role (
    Id UUID PRIMARY KEY,
    RoleCode TEXT,
    RoleName TEXT,
    Descriptions TEXT,
    CreatedDate TIMESTAMP,
    ModifiedDate TIMESTAMP,
);

--This allows you to query DepartmentCode without requiring ALLOW FILTERING
CREATE INDEX role_code_idx ON role (RoleCode);

--This is script to insert data into role table:
INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'ADMIN', 'Administrator', 'Has full system access', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'HR', 'Human Resources Manager', 'Manages employee relations', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'DEV', 'Developer', 'Responsible for software development', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'SALES', 'Sales Manager', 'Handles sales and client relationships', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'IT', 'IT Support', 'Maintains company IT infrastructure', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'FIN', 'Finance Manager', 'Manages company financial operations', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'MKT', 'Marketing Specialist', 'Responsible for marketing and promotions', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'OPS', 'Operations Manager', 'Oversees daily business operations', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'QA', 'Quality Assurance', 'Ensures product quality and testing', toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, CreatedDate, ModifiedDate)
VALUES (uuid(), 'R&D', 'Research and Development', 'Works on new innovations and improvements', toTimestamp(now()), toTimestamp(now()));



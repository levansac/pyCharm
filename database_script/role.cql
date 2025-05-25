CREATE TABLE role (
    Id UUID PRIMARY KEY,
    RoleCode TEXT,
    RoleName TEXT,
    Status TINYINT,
    Descriptions TEXT,
    CreatedDate TIMESTAMP,
    ModifiedDate TIMESTAMP
);

--This allows you to query DepartmentCode without requiring ALLOW FILTERING

CREATE INDEX IF NOT EXISTS idx_rolecode ON role (RoleCode);
CREATE INDEX IF NOT EXISTS idx_rolename ON role (RoleName);
CREATE INDEX IF NOT EXISTS idx_status ON role (Status);


--This is script to insert data into role table:
INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'ADMIN', 'Administrator', 'Has full system access', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'HR', 'Human Resources Manager', 'Manages employee relations', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'DEV', 'Developer', 'Responsible for software development', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'SALES', 'Sales Manager', 'Handles sales and client relationships', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'IT', 'IT Support', 'Maintains company IT infrastructure', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'FIN', 'Finance Manager', 'Manages company financial operations', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'MKT', 'Marketing Specialist', 'Responsible for marketing and promotions', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'OPS', 'Operations Manager', 'Oversees daily business operations', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'QA', 'Quality Assurance', 'Ensures product quality and testing', 0, toTimestamp(now()), toTimestamp(now()));

INSERT INTO role (Id, RoleCode, RoleName, Descriptions, Status, CreatedDate, ModifiedDate)
VALUES (uuid(), 'R&D', 'Research and Development', 'Works on new innovations and improvements', 0, toTimestamp(now()), toTimestamp(now()));



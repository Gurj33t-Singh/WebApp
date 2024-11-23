CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE TABLE data (
    uuid_field UUID DEFAULT gen_random_uuid(),  -- UUID field with auto-generated value
    phone_number VARCHAR(15) PRIMARY KEY,  -- Field for phone number as the primary key
    field1 TEXT,
    field2 TEXT,
    field3 TEXT,
    field4 TEXT,
    field5 TEXT,
    field6 TEXT,
    field7 TEXT,
    field8 TEXT,
    field9 TEXT,
    field10 TEXT
);

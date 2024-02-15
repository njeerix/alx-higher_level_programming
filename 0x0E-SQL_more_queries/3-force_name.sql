-- Create the table force_name with id INT and name VARCHAR(256)
-- Create the table only if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

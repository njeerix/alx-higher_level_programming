-- Create the table id_not_null with id INT and name VARCHAR(256)
-- Create the table only if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

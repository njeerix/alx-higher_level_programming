-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
Use hbtn_0d_usa;

-- Create the table states only if it does not already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE KEY unique_name (name)
);

-- Clear any existing data from the states table
DELETE FROM states;

-- Insert sample data into the states table, ignoring duplicates
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');

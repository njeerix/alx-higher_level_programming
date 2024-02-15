-- Check if the hbtn_0d_usa database exists, if not, create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert sample data into the states table if it's empty
INSERT IGNORE INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');

-- Check if the cities table exists, if not, create it
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Clear any existsing data from the cities table
DELETE FROM cities;

-- Insert sample data into the cities table
INSERT INTO cities (state_id, name) VALUES
(1, 'San Francisco'), (1, 'San Jose'), (2, 'Page'),
(3, 'Paris'), (3, 'Houston'), (3, 'Dallas');

-- List all cities and their corresponding states
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

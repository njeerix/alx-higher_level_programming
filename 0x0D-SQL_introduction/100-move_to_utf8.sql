-- Select the hbtn_0c_0 database
USE hbtn_0c_0;

-- Alter the database hbtn_0c_0 to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

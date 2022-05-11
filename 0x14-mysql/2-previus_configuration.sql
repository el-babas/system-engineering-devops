--# Create a new database.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id INT, name VARCHAR(256));
INSERT INTO nexus6 (id, name) VALUES (1, "Leon");
GRANT SELECT ON tyrell_corp.* TO holberton_user@localhost;

--mysql -u root -p
-- Create user for replication
CREATE USER IF NOT EXISTS replica_user@'%' IDENTIFIED BY 'replica_user';
-- Add permission to replication.
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
-- Add privileged select in mysql
GRANT SELECT ON mysql.* TO holberton_user@localhost;

-- this script creates database hbtn_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user user_0d_2 with password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- this user has only SELECT privilege in the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

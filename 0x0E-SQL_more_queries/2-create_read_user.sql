-- creates a database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creating user with SELECT privileges only
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- granting permissions to user_0d_2 for database hbtn_0d_2
GRANT SELLECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
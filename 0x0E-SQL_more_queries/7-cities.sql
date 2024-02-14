-- Creates a database that doesn't overwrite pre-existing versions
CREATES DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switches the active database
USE hbtn_0d_usa;
-- Creates a table with column that is foreign key.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id),
    FOREIGN KEY(state_id)
        REFERENCE states(id)
);
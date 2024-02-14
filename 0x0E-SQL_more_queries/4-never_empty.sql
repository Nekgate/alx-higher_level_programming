-- Creates a table with a constraint on column and another
-- column that is never empty when given a NULL value.
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
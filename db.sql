CREATE TABLE IF NOT EXISTS dw (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    fhd BLOB DEFAULT NULL,
    shd BLOB DEFAULT NULL
);
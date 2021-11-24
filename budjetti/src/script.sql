"""Create SQL table"""
CREATE TABLE stores
    (id INTEGER PRIMARY KEY, storenumber INTEGER, password TEXT);

INSERT INTO stores
    (storenumber, password) VALUES (?,?)


DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (name, password) VALUES ('admin', 'admin123');
INSERT INTO users (name, password) VALUES ('maitree', 'maitree123');
INSERT INTO users (name, password) VALUES ('prachi', 'prachi123');

DROP TABLE IF EXISTS data;

CREATE TABLE data (
    data TEXT
);

INSERT INTO data VALUES ('abc123');
INSERT INTO data VALUES ('xyz459');
INSERT INTO data VALUES ('mms713');

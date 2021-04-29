DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS service;
DROP TABLE IF EXISTS campus;
DROP TABLE IF EXISTS category;

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE service(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    resource TEXT NOT NULL REFERENCES category(resource_type), 
    email TEXT NOT NULL,
    location TEXT NOT NULL REFERENCES campus(name),
    description TEXT,
    hours TEXT
);


CREATE TABLE category(
    resource_type TEXT PRIMARY KEY NOT NULL
);

INSERT INTO category (resource_type) VALUES 
    ("Food"),
    ("Wellness"),
    ("Housing"),
    ("Finance"),
    ("Other");


CREATE TABLE campus(
    name TEXT PRIMARY KEY NOT NULL
);

INSERT INTO campus (name) VALUES 
    ('UCSC'),
    ('UCB'),
    ('UCM'),
    ('UCR'),
    ('UCSB'),
    ('UCD'),
    ('UCSF'),
    ('UCLA'),
    ('UCI'),
    ('UCSD');
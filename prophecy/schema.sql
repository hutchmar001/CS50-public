CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    house TEXT,
    head TEXT,
    PRIMARY KEY(house)
);

CREATE TABLE assignments (
    id INTEGER,
    house TEXT,
);
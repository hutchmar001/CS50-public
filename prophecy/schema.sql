CREATE TABLE student (
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
    FOREIGN KEY (id) REFERENCES student(id),
    FOREIGN KEY (house) REFERENCES houses(house)
);
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
    student_id INTEGER,
    student_house TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (student_house) REFERENCES houses(house)
);
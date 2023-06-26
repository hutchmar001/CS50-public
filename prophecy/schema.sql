CREATE TABLE student (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(student_id)
);

CREATE TABLE houses (
    house TEXT,
    head TEXT,
    PRIMARY KEY(house)
);

CREATE TABLE assignments (
    student_id INTEGER,
    assigned_house TEXT,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (assigned_house) REFERENCES houses(house)
);
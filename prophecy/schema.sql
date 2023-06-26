CREATE TABLE "student" (
    student_id INTEGER,
    "student_name" TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE "houses" (
    "house" TEXT,
    "head" TEXT,
    PRIMARY KEY(house)
);

CREATE TABLE "assignments" (
    "id" INTEGER,
    "assigned_house" TEXT,
    FOREIGN KEY (id) REFERENCES student(student_id)
    FOREIGN KEY (assigned_house) REFERENCES houses(house)
);
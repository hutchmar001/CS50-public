CREATE TABLE "student" (
    "id" INTEGER,
    "student_name" TEXT,
    FOREIGN KEY (id) REFERENCES students(id)
    FOREIGN KEY (student_name) REFERENCES students(student_name)
);

CREATE TABLE "houses" (
    "house" TEXT,
    "head" TEXT,
    FOREIGN KEY (house) REFERENCES students(house)
    FOREIGN KEY (head) REFERENCES students(head)
);

CREATE TABLE "assignments" (
    "id" INTEGER,
    "house" TEXT,
    FOREIGN KEY (id) REFERENCES students(id)
    FOREIGN KEY (house) REFERENCES students(house)
);
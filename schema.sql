CREATE DATABASE IF NOT EXISTS student_management_db;
USE student_management_db;

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    date_of_birth DATE
);

CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL UNIQUE,
    duration VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    marks DECIMAL(5,2) NOT NULL,
    grade VARCHAR(2) NOT NULL,
    CONSTRAINT fk_result_student FOREIGN KEY(student_id)
        REFERENCES students(student_id) ON DELETE RESTRICT,
    CONSTRAINT fk_result_course FOREIGN KEY(course_id)
        REFERENCES courses(course_id) ON DELETE RESTRICT,
    CONSTRAINT chk_marks CHECK(marks >= 0 AND marks <= 100),
    CONSTRAINT unique_student_course UNIQUE(student_id,course_id)
);

-- Optional sample data. Run only if you want demo records.
-- INSERT INTO students(student_name,email,phone,date_of_birth)
-- VALUES ('Ranjith','ranjith@example.com','9876543210','2002-05-10');

-- INSERT INTO courses(course_name,duration)
-- VALUES ('Python','3 Months'),('MySQL','2 Months');

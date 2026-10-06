USE student_management_db;

-- View tables
SHOW TABLES;

-- Basic SELECT
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM results;

-- JOIN report
SELECT s.student_name, c.course_name, r.marks, r.grade
FROM results r
INNER JOIN students s ON r.student_id=s.student_id
INNER JOIN courses c ON r.course_id=c.course_id;

-- Highest mark
SELECT MAX(marks) AS highest_mark FROM results;

-- Average marks
SELECT ROUND(AVG(marks),2) AS average_marks FROM results;

-- Students above 80
SELECT s.student_name, c.course_name, r.marks
FROM results r
INNER JOIN students s ON r.student_id=s.student_id
INNER JOIN courses c ON r.course_id=c.course_id
WHERE r.marks > 80
ORDER BY r.marks DESC;

-- Number of students in each course
SELECT c.course_name, COUNT(r.student_id) AS student_count
FROM courses c
LEFT JOIN results r ON c.course_id=r.course_id
GROUP BY c.course_id,c.course_name;

-- Failed students
SELECT s.student_name,c.course_name,r.marks,r.grade
FROM results r
INNER JOIN students s ON r.student_id=s.student_id
INNER JOIN courses c ON r.course_id=c.course_id
WHERE r.marks < 50;

# Student Course & Result Management System

## 1. Project Objective
A terminal-based Python and MySQL application for managing students, courses, marks and results.

## 2. Technologies
- Python
- MySQL
- SQL
- mysql-connector-python

## 3. Features
### Student Management
- Add student
- View all students
- View student by ID
- Search by name
- Update student
- Delete student

### Course Management
- Add course
- View courses
- Search course
- Update course
- Delete course

### Result Management
- Add result
- Automatic grade calculation
- View all results
- View results by student
- View results by course

### Reports
- Students with course and marks
- Highest mark
- Average marks
- Students above 80
- Number of students per course
- Failed students

## 4. Grade System
90-100 = A+
80-89 = A
70-79 = B
60-69 = C
50-59 = D
Below 50 = F

## 5. Database Structure
students -> results <- courses

The results table contains foreign keys to students and courses.

## 6. Setup

### Step 1: Install Python
Install Python 3.x and make sure Python is available in the VS Code terminal.

### Step 2: Install dependency
Run:
    pip install -r requirements.txt

### Step 3: Create MySQL database
Open MySQL Workbench and execute `schema.sql`.

### Step 4: Set MySQL password
Open `database.py` and change:
    "password": "YOUR_MYSQL_PASSWORD"
to your actual MySQL root password.

### Step 5: Run
In the VS Code terminal:
    python main.py

## 7. Project Structure
student_management_system/
    main.py
    database.py
    student.py
    course.py
    result.py
    reports.py
    schema.sql
    requirements.txt
    README.md

## 8. Application Flow
Start -> Main Menu -> Student/Course/Result/Reports -> Database -> Display Result -> Back to Menu -> Exit

## 9. Validation
- Empty student name is rejected.
- Invalid email is rejected.
- IDs must be integers.
- Marks must be between 0 and 100.
- Duplicate emails are rejected.
- Duplicate student-course results are rejected.
- Missing students/courses are handled.

## 10. SQL Concepts Demonstrated
- CREATE DATABASE / TABLE
- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- LIKE
- INNER JOIN
- COUNT
- AVG
- MAX
- GROUP BY
- ORDER BY
- Foreign keys
- Unique constraints

## 11. Demo Steps
1. Add two courses.
2. Add two students.
3. View students.
4. Add results.
5. View all results.
6. Run each report.
7. Test invalid email.
8. Test marks above 100.
9. Test a non-existing student ID.
10. Show the database tables in MySQL Workbench.

## 12. Mentor Explanation
The project uses separate Python modules to keep the code organized. `database.py` handles MySQL connectivity. `student.py`, `course.py`, and `result.py` contain their respective CRUD operations. `reports.py` contains SQL report queries. `main.py` controls the terminal menus. Results are linked to students and courses using foreign keys. Grade is calculated automatically from marks.

## 13. Important
Do not submit code you cannot explain. Understand the database relationship, CRUD operations, JOIN queries, grade calculation and validation before the demo.

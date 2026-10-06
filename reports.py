from database import get_connection

def run_query(title, sql, params=None):
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute(sql, params or ())
        rows=cursor.fetchall()
        print(f"\n===== {title} =====")
        if not rows: print("No data found."); return
        for row in rows: print(" | ".join(str(x) for x in row))
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def report_all_students():
    run_query("ALL STUDENTS WITH COURSE AND MARKS", """
        SELECT s.student_name,c.course_name,r.marks,r.grade
        FROM results r
        INNER JOIN students s ON r.student_id=s.student_id
        INNER JOIN courses c ON r.course_id=c.course_id
        ORDER BY s.student_name
    """)

def report_highest_mark():
    run_query("HIGHEST MARK", "SELECT MAX(marks) AS highest_mark FROM results")

def report_average_marks():
    run_query("AVERAGE MARKS", "SELECT ROUND(AVG(marks),2) AS average_marks FROM results")

def report_above_80():
    run_query("STUDENTS ABOVE 80", """
        SELECT s.student_name,c.course_name,r.marks
        FROM results r
        INNER JOIN students s ON r.student_id=s.student_id
        INNER JOIN courses c ON r.course_id=c.course_id
        WHERE r.marks > 80
        ORDER BY r.marks DESC
    """)

def report_students_per_course():
    run_query("NUMBER OF STUDENTS IN EACH COURSE", """
        SELECT c.course_name,COUNT(r.student_id) AS student_count
        FROM courses c
        LEFT JOIN results r ON c.course_id=r.course_id
        GROUP BY c.course_id,c.course_name
        ORDER BY student_count DESC
    """)

def report_failed_students():
    run_query("FAILED STUDENTS", """
        SELECT s.student_name,c.course_name,r.marks,r.grade
        FROM results r
        INNER JOIN students s ON r.student_id=s.student_id
        INNER JOIN courses c ON r.course_id=c.course_id
        WHERE r.marks < 50
        ORDER BY r.marks
    """)

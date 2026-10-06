from database import get_connection

def calculate_grade(marks):
    if marks >= 90: return "A+"
    if marks >= 80: return "A"
    if marks >= 70: return "B"
    if marks >= 60: return "C"
    if marks >= 50: return "D"
    return "F"

def add_result():
    sid=input("Enter student ID: ").strip()
    cid=input("Enter course ID: ").strip()
    marks_text=input("Enter marks (0-100): ").strip()
    if not sid.isdigit() or not cid.isdigit():
        print("Student ID and Course ID must be valid integers."); return
    try: marks=float(marks_text)
    except ValueError:
        print("Marks must be numeric."); return
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100."); return

    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT student_id FROM students WHERE student_id=%s",(int(sid),))
        if not cursor.fetchone(): print("Student not found."); return
        cursor.execute("SELECT course_id FROM courses WHERE course_id=%s",(int(cid),))
        if not cursor.fetchone(): print("Course not found."); return
        cursor.execute("SELECT result_id FROM results WHERE student_id=%s AND course_id=%s",(int(sid),int(cid)))
        if cursor.fetchone(): print("Result already exists for this student and course."); return
        grade=calculate_grade(marks)
        cursor.execute("INSERT INTO results(student_id,course_id,marks,grade) VALUES(%s,%s,%s,%s)",
                       (int(sid),int(cid),marks,grade))
        conn.commit(); print(f"Result added successfully. Grade: {grade}")
    except Exception as e:
        conn.rollback(); print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def view_all_results():
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("""SELECT r.result_id,s.student_name,c.course_name,r.marks,r.grade
                          FROM results r
                          INNER JOIN students s ON r.student_id=s.student_id
                          INNER JOIN courses c ON r.course_id=c.course_id
                          ORDER BY r.result_id""")
        rows=cursor.fetchall()
        if not rows: print("No results found."); return
        print("\n"+"-"*80)
        print(f"{'ID':<8}{'Student':<25}{'Course':<25}{'Marks':<10}{'Grade':<8}")
        print("-"*80)
        for r in rows: print(f"{r[0]:<8}{r[1]:<25}{r[2]:<25}{r[3]:<10}{r[4]:<8}")
        print("-"*80)
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def view_results_by_student():
    sid=input("Enter student ID: ").strip()
    if not sid.isdigit(): print("Student ID must be a valid integer."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("""SELECT s.student_name,c.course_name,r.marks,r.grade
                          FROM results r INNER JOIN students s ON r.student_id=s.student_id
                          INNER JOIN courses c ON r.course_id=c.course_id
                          WHERE r.student_id=%s""",(int(sid),))
        rows=cursor.fetchall()
        if not rows: print("No results found for this student."); return
        for r in rows: print(f"Student: {r[0]} | Course: {r[1]} | Marks: {r[2]} | Grade: {r[3]}")
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def view_results_by_course():
    cid=input("Enter course ID: ").strip()
    if not cid.isdigit(): print("Course ID must be a valid integer."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("""SELECT s.student_name,c.course_name,r.marks,r.grade
                          FROM results r INNER JOIN students s ON r.student_id=s.student_id
                          INNER JOIN courses c ON r.course_id=c.course_id
                          WHERE r.course_id=%s ORDER BY r.marks DESC""",(int(cid),))
        rows=cursor.fetchall()
        if not rows: print("No results found for this course."); return
        for r in rows: print(f"Student: {r[0]} | Course: {r[1]} | Marks: {r[2]} | Grade: {r[3]}")
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

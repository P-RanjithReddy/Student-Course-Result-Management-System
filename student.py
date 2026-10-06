import re
from database import get_connection

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

def valid_email(email):
    return bool(re.match(EMAIL_PATTERN, email))

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return
    email = input("Enter email: ").strip()
    if not valid_email(email):
        print("Invalid email format.")
        return
    phone = input("Enter phone: ").strip()
    dob = input("Enter date of birth (YYYY-MM-DD): ").strip()

    conn = get_connection()
    if not conn: return
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO students
            (student_name,email,phone,date_of_birth)
            VALUES (%s,%s,%s,%s)""", (name,email,phone,dob))
        conn.commit()
        print(f"Student added successfully. Student ID: {cursor.lastrowid}")
    except Exception as e:
        conn.rollback()
        print("Duplicate email." if "Duplicate entry" in str(e) else f"Error: {e}")
    finally:
        cursor.close(); conn.close()

def view_students():
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT student_id,student_name,email,phone,date_of_birth FROM students ORDER BY student_id")
        rows=cursor.fetchall()
        if not rows:
            print("No students found."); return
        print("\n"+"-"*90)
        print(f"{'ID':<6}{'Name':<25}{'Email':<30}{'Phone':<15}{'DOB':<12}")
        print("-"*90)
        for r in rows:
            print(f"{r[0]:<6}{r[1]:<25}{r[2]:<30}{r[3] or '':<15}{str(r[4] or ''):<12}")
        print("-"*90)
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def view_student_by_id():
    sid=input("Enter student ID: ").strip()
    if not sid.isdigit():
        print("Student ID must be a valid integer."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE student_id=%s",(int(sid),))
        r=cursor.fetchone()
        if r:
            print(f"\nID: {r[0]}\nName: {r[1]}\nEmail: {r[2]}\nPhone: {r[3]}\nDOB: {r[4]}")
        else: print("Student not found.")
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def search_student():
    name=input("Enter student name to search: ").strip()
    if not name:
        print("Search name cannot be empty."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("""SELECT student_id,student_name,email,phone,date_of_birth
                          FROM students WHERE student_name LIKE %s ORDER BY student_name""",(f"%{name}%",))
        rows=cursor.fetchall()
        if not rows: print("No matching students found."); return
        for r in rows:
            print(f"ID: {r[0]} | Name: {r[1]} | Email: {r[2]} | Phone: {r[3]} | DOB: {r[4]}")
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def update_student():
    sid=input("Enter student ID to update: ").strip()
    if not sid.isdigit():
        print("Student ID must be a valid integer."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE student_id=%s",(int(sid),))
        if not cursor.fetchone():
            print("Student not found."); return
        name=input("Enter new name: ").strip()
        email=input("Enter new email: ").strip()
        phone=input("Enter new phone: ").strip()
        if not name: print("Student name cannot be empty."); return
        if not valid_email(email): print("Invalid email format."); return
        cursor.execute("""UPDATE students SET student_name=%s,email=%s,phone=%s
                          WHERE student_id=%s""",(name,email,phone,int(sid)))
        conn.commit(); print("Student updated successfully.")
    except Exception as e:
        conn.rollback()
        print("Duplicate email." if "Duplicate entry" in str(e) else f"Error: {e}")
    finally: cursor.close(); conn.close()

def delete_student():
    sid=input("Enter student ID to delete: ").strip()
    if not sid.isdigit():
        print("Student ID must be a valid integer."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT student_name FROM students WHERE student_id=%s",(int(sid),))
        r=cursor.fetchone()
        if not r: print("Student not found."); return
        if input(f"Delete '{r[0]}'? (y/n): ").strip().lower()!="y":
            print("Delete cancelled."); return
        cursor.execute("DELETE FROM students WHERE student_id=%s",(int(sid),))
        conn.commit(); print("Student deleted successfully.")
    except Exception as e:
        conn.rollback()
        print("Cannot delete student because results exist." if "foreign key" in str(e).lower() else f"Error: {e}")
    finally: cursor.close(); conn.close()

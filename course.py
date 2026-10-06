from database import get_connection

def add_course():
    name=input("Enter course name: ").strip()
    duration=input("Enter course duration: ").strip()
    if not name or not duration:
        print("Course name and duration cannot be empty."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO courses(course_name,duration) VALUES(%s,%s)",(name,duration))
        conn.commit(); print(f"Course added successfully. Course ID: {cursor.lastrowid}")
    except Exception as e:
        conn.rollback()
        print("Course already exists." if "Duplicate entry" in str(e) else f"Error: {e}")
    finally: cursor.close(); conn.close()

def view_courses():
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT course_id,course_name,duration FROM courses ORDER BY course_id")
        rows=cursor.fetchall()
        if not rows: print("No courses found."); return
        print("\n"+"-"*60)
        print(f"{'ID':<8}{'Course Name':<30}{'Duration':<20}")
        print("-"*60)
        for r in rows: print(f"{r[0]:<8}{r[1]:<30}{r[2]:<20}")
        print("-"*60)
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def search_course():
    name=input("Enter course name to search: ").strip()
    if not name: print("Search name cannot be empty."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT course_id,course_name,duration FROM courses WHERE course_name LIKE %s",(f"%{name}%",))
        rows=cursor.fetchall()
        if not rows: print("No matching courses found."); return
        for r in rows: print(f"ID: {r[0]} | Course: {r[1]} | Duration: {r[2]}")
    except Exception as e: print(f"Error: {e}")
    finally: cursor.close(); conn.close()

def update_course():
    cid=input("Enter course ID to update: ").strip()
    if not cid.isdigit(): print("Course ID must be a valid integer."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM courses WHERE course_id=%s",(int(cid),))
        if not cursor.fetchone(): print("Course not found."); return
        name=input("Enter new course name: ").strip()
        duration=input("Enter new duration: ").strip()
        if not name or not duration: print("Fields cannot be empty."); return
        cursor.execute("UPDATE courses SET course_name=%s,duration=%s WHERE course_id=%s",(name,duration,int(cid)))
        conn.commit(); print("Course updated successfully.")
    except Exception as e:
        conn.rollback()
        print("Course already exists." if "Duplicate entry" in str(e) else f"Error: {e}")
    finally: cursor.close(); conn.close()

def delete_course():
    cid=input("Enter course ID to delete: ").strip()
    if not cid.isdigit(): print("Course ID must be a valid integer."); return
    conn=get_connection()
    if not conn: return
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT course_name FROM courses WHERE course_id=%s",(int(cid),))
        r=cursor.fetchone()
        if not r: print("Course not found."); return
        if input(f"Delete '{r[0]}'? (y/n): ").strip().lower()!="y":
            print("Delete cancelled."); return
        cursor.execute("DELETE FROM courses WHERE course_id=%s",(int(cid),))
        conn.commit(); print("Course deleted successfully.")
    except Exception as e:
        conn.rollback()
        print("Cannot delete course because results exist." if "foreign key" in str(e).lower() else f"Error: {e}")
    finally: cursor.close(); conn.close()

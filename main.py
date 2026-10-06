from student import add_student,view_students,view_student_by_id,search_student,update_student,delete_student
from course import add_course,view_courses,search_course,update_course,delete_course
from result import add_result,view_all_results,view_results_by_student,view_results_by_course
from reports import report_all_students,report_highest_mark,report_average_marks,report_above_80,report_students_per_course,report_failed_students

def student_menu():
    while True:
        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. View Student By ID")
        print("4. Search Student")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Back")
        choice=input("Enter your choice: ").strip()
        actions={"1":add_student,"2":view_students,"3":view_student_by_id,"4":search_student,"5":update_student,"6":delete_student}
        if choice in actions: actions[choice]()
        elif choice=="7": break
        else: print("Invalid menu option.")

def course_menu():
    while True:
        print("\n========== COURSE MANAGEMENT ==========")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Search Course")
        print("4. Update Course")
        print("5. Delete Course")
        print("6. Back")
        choice=input("Enter your choice: ").strip()
        actions={"1":add_course,"2":view_courses,"3":search_course,"4":update_course,"5":delete_course}
        if choice in actions: actions[choice]()
        elif choice=="6": break
        else: print("Invalid menu option.")

def result_menu():
    while True:
        print("\n========== RESULT MANAGEMENT ==========")
        print("1. Add Result")
        print("2. View All Results")
        print("3. View Results By Student")
        print("4. View Results By Course")
        print("5. Back")
        choice=input("Enter your choice: ").strip()
        actions={"1":add_result,"2":view_all_results,"3":view_results_by_student,"4":view_results_by_course}
        if choice in actions: actions[choice]()
        elif choice=="5": break
        else: print("Invalid menu option.")

def report_menu():
    while True:
        print("\n========== REPORTS ==========")
        print("1. All Students With Course And Marks")
        print("2. Highest Mark")
        print("3. Average Marks")
        print("4. Students Above 80")
        print("5. Number Of Students In Each Course")
        print("6. Failed Students")
        print("7. Back")
        choice=input("Enter your choice: ").strip()
        actions={"1":report_all_students,"2":report_highest_mark,"3":report_average_marks,
                 "4":report_above_80,"5":report_students_per_course,"6":report_failed_students}
        if choice in actions: actions[choice]()
        elif choice=="7": break
        else: print("Invalid menu option.")

def main():
    while True:
        print("\n========================================")
        print(" STUDENT COURSE & RESULT MANAGEMENT")
        print("========================================")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Result Management")
        print("4. Reports")
        print("5. Exit")
        choice=input("Enter your choice: ").strip()
        if choice=="1": student_menu()
        elif choice=="2": course_menu()
        elif choice=="3": result_menu()
        elif choice=="4": report_menu()
        elif choice=="5":
            print("Thank you for using the system!")
            break
        else: print("Invalid menu option. Please enter 1-5.")

if __name__=="__main__":
    main()

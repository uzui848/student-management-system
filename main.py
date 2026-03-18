
from storage import load_data
from student_manager import *


student = load_data()


def menu_option():

    while True:

        print("\n1. add student")
        print("2. view student")
        print("3. search student")
        print("4. update student marks")
        print("5. delete student")
        print("6. topper student")
        print("7. average marks")
        print("8. total student")
        print("9. exit")

        choice = int(input("enter your choice: "))

        if choice == 1:
            student_details(student)

        elif choice == 2:
            student_view(student)

        elif choice == 3:
            search_student(student)

        elif choice == 4:
            update_student(student)

        elif choice == 5:
            del_student(student)

        elif choice == 6:
            topper_student(student)
        
        elif choice == 7:
            student_average(student)

        elif choice == 8:
            student_count(student)

        elif choice == 8:
            break

        else:
            print("invalid option")


menu_option()
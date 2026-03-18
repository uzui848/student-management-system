
from storage import save_data


def student_details(student):

    student_id = int(input("enter student ID: "))

    if student_id in student:
        print("student ID already exists")
        return

    stu_name = input("enter student name: ")
    stu_marks = float(input("enter student marks: "))

    student[student_id] = {
        "stu_name": stu_name,
        "stu_marks": stu_marks
    }

    save_data(student)
    print("student added")


def student_view(student):

    if not student:
        print("no student found")
        return

    for sid, info in student.items():
        print("---------------------")
        print("ID:", sid)
        print("Name:", info["stu_name"])
        print("Marks:", info["stu_marks"])
        print("---------------------")


def search_student(student):

    student_id = int(input("enter the student id to search: "))

    if student_id in student:
        data = student[student_id]

        print("student Id:", student_id)
        print("student name:", data["stu_name"])
        print("student marks:", data["stu_marks"])

    else:
        print("student data not exist")


def update_student(student):

    student_id = int(input("enter the student ID: "))

    if student_id in student:
        new_marks = float(input("enter new marks: "))

        student[student_id]["stu_marks"] = new_marks

        save_data(student)
        print("marks updated")

    else:
        print("student not found")


def del_student(student):

    stu_del = int(input("enter the student ID: "))

    if stu_del in student:
        del student[stu_del]

        save_data(student)
        print("student deleted")

    else:
        print("not found")


def topper_student(student):

    if not student:
        print("no students available")
        return

    highest = -1
    topper_name = ""
    topper_id = None

    for student_id, info in student.items():

        marks = info["stu_marks"]

        if marks > highest:
            highest = marks
            topper_name = info["stu_name"]
            topper_id = student_id

    print("Topper:", topper_name)
    print("ID:", topper_id)
    print("Marks:", highest)

# student average:

def student_average(student):
    if not student :
        print("invaild entry")
        return
    
    total = 0

    for student_id in student:

        total += student[student_id]["stu_marks"]
    average = total / len(student)

    print("average marks: ",average)


def student_count(student):
    for student_id in student:
        word = len(student)
    
    print("total student on the institute:" ,word)
    
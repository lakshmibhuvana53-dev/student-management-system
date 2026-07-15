# Student management system
students_details = [
    {
        "Name": "Sara",
        "Class": "10th",
        "Roll_No": 1,
        "Marks" : 75
    },
    {
        "Name": "Haroon",
        "Class": "10th",
        "Roll_No": 2,
        "Marks" :80
    },
    {
        "Name": "Ali",
        "Class": "10th",
        "Roll_No": 3,
        "Marks" : 95
    },
    {
        "Name": "Zohara",
        "Class": "10th",
        "Roll_No": 4,
        "Marks" : 93
    },
    {
        "Name": "Arav",
        "Class": "10th",
        "Roll_No": 5,
        "Marks" : 59
    },
    {
        "Name": "Ayesha",
        "Class": "10th",
        "Roll_No": 6,
        "Marks" : 67
    },
    {
        "Name": "osman",
        "Class": "10th",
        "Roll_No": 7,
        "Marks" : 85
    },
    {
        "Name": "Fatima",
        "Class": "10th",
        "Roll_No": 8,
        "Marks" : 77
    },
    {
        "Name": "Salma",
        "Class": "10th",
        "Roll_No": 9,
        "Marks" : 100
    },
    {
        "Name": "Babajaan",
        "Class": "10th",
        "Roll_No": 10,
        "Marks" : 99
    }

]
def details():
    user_input = int(input("Enter Roll_number to know the details of a student: "))
    for student in students_details:
        if student["Roll_No"] == int(user_input):
            print(f"Name: {student['Name']}\nClass: {student['Class']}\nRoll_No: {student['Roll_No']}\nMarks: {student['Marks']}")
            break
            
    else:
         print("Student not found.")

            

def check_topper():
    max_marks = 0
    topper = ""
    for student in students_details:
        if student["Marks"] > max_marks:
            max_marks = student["Marks"]
            topper = student["Name"]
    print("Topper:", topper)
    print("Marks:", max_marks)
def above_85():
    print("The Students above 85 marks are:\n")
    for student in students_details:
        if student["Marks"] >= 85:
            print(f"Name: {student['Name']}\nMarks: {student['Marks']}\n")

def add_student():
    print("To add a student,You need to provide the following details:\n")
    name = input("Enter the name of the student: ")
    class_name = input("Enter the class of the student: ")
    roll_no = int(input("Enter the roll number of the student: "))
    marks = int(input("Enter the marks of the student: "))
    for student in students_details:
        if roll_no == student["Roll_No"]:
            print("Roll number already exists. Please enter a unique roll number.")
            return
    new_student = {
        "Name": name,
        "Class": class_name,
        "Roll_No": roll_no,
        "Marks": marks
    }
    students_details.append(new_student)
    print("Student added successfully!")

def delete_student():
    roll_no = int(input("Enter the roll number of the student to delete: "))
    for student in students_details:
        if student["Roll_No"] == roll_no:
            print(f"Name: {student['Name']}\nClass: {student['Class']}\nRoll_No: {student['Roll_No']}\nMarks: {student['Marks']}")
            confirmation = input("Are you sure you want to delete this student? (Yes/No)").lower()
            if confirmation == "yes":
                students_details.remove(student)
                print("Student deleted successfully!")
                break
            else:
                print("Deletion cancelled.")

    else:
        print("Student not found.")

def update_student():
    roll_no = int(input("Enter the roll number of the student to update: "))
    for student in students_details:
        if student["Roll_No"] == roll_no:
            print("Current details of the student.\n")
            print(f"Name: {student['Name']}\nClass: {student['Class']}\nRoll_No: {student['Roll_No']}\nMarks: {student['Marks']}")
            name = input("Enter the new name of the student (leave blank to keep current): ")
            class_name = input("Enter the new class of the student (leave blank to keep current): ")
            marks = input("Enter the new marks of the student (leave blank to keep current): ")
            if name:
                student["Name"] = name
            if class_name:
                student["Class"] = class_name
            if marks:
                student["Marks"] = int(marks)
            print("Student details updated successfully!")
            break
            
    else:
        print("Student not found.")

def work():
    exit_program = False
    while not exit_program:

        print("Welcome to the Student Management System!")
        user_choice = input("Enter '1' to check topper\nEnter '2' to check student details\nEnter '3' To see students above 85 marks\nEnter '4' To add a student\nEnter '5' to delete a student\nEnter '6' To update a student details\nEnter '7' to Exit\n")
        if user_choice == "1":
            check_topper()
        elif user_choice == "2":
            details()
        elif user_choice == "3":
            above_85()
        elif user_choice == "4":
            add_student()
        elif user_choice == "5":
            delete_student()
        elif user_choice == "6":
            update_student()
        elif user_choice == "7":
            print("Exiting the program.")
            exit_program = True
        else:
            print("Invalid choice. Please try again.")
    print("Thank you for using the Student Management System!")
work()

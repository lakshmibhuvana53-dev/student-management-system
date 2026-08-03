class Student:
    def __init__(self, name, reg_no, class_name, marks):
        self.name = name
        self.reg_no = reg_no
        self.class_name = class_name
        self.marks = marks

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Reg_No : {self.reg_no}")
        print(f"Class  : {self.class_name}")
        print(f"Marks  : {self.marks}")

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        for existing_student in self.students:
            if existing_student.reg_no == student.reg_no:
                print(f"Student with Reg_no {student.reg_no} already exist\nsorry {student.name}, You cannot be admitted ")
                return
        self.students.append(student)

    def search_student(self):
        try:
            user_input = int(input("Enter the Reg_no of the student to search : "))
        except ValueError:
            print("Invalid input give only numbers.")
            return
        
        for existing_student in self.students:
            if existing_student.reg_no == user_input:
                existing_student.display()
                return
        else:
            print("Student not found")

    def display_students(self):
        if not self.students:
            print("No student found !")
            return
        for student in self.students:
            student.display()
            print("-" *30)

    def update_details(self):
        try:
            user_input = int(input("Enter the Reg_no of the student to update details : "))
        except ValueError:
            print("Invalid input give only numbers.")
            return
        
                    
        for student in self.students:
            if student.reg_no == user_input:
                student.display()
                field = input("What do you want to update""\n(name, class_name, marks): ").lower()
                if field == "marks":
                    try:
                        new_value = int(input("Enter new value : "))
                    except ValueError:
                        print("Invalid input give only numbers.")
                        return

                else :
                    new_value = input("Enter new value: ")  

                if hasattr(student,field):
                    setattr(student,field,new_value)
                    student.display()
                    print("student details is updated successfully")
                else:
                    print("Invalid field name.")
                return
        print("student not found") 

    def delete_student(self):
        try:
            user_input = int(input("Enter the Reg_no of the student to be deleted: "))
        except ValueError:
            print("Invalid input give only numbers.")
            return
        
        
        for student in self.students:
            if student.reg_no == user_input:
                student.display()
                choice = input("Enter 'yes' to confirm or 'no' to stop : ").lower()
                if choice == "yes":
                    self.students.remove(student)
                    print("Successfully deleted the student")
                    return
                elif choice == "no":
                    print("Deletion cancelled.")
                    return
                else:
                    print("Invalid choice")
                    return
                    
        else:

            print("Student not found")
 # Load student data from the file into the students list.
    def load_students(self):
        try:
            with open("student.txt","r")as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    name, reg_no, class_name, marks = line.split(",")
                    student = Student(name, int(reg_no), class_name, int(marks))
                    self.students.append(student)
                print("Student data loaded successfully from the file.")
        except FileNotFoundError:
            print("No existing student data found. Starting with an empty list.")
        except Exception as e:
            print(f"Error while loading students: {e}")


# save student data from the students list to the file.
    def save_students(self):
        try:

            with open("student.txt","w")as file:
                for student in self.students:
                    file.write(f"{student.name},{student.reg_no},{student.class_name},{student.marks}\n")
                print("Student data saved successfully to the file.")    
        except Exception as e:
            print(f"Error while saving students: {e}")

        
    def system_menu(self):
        exit_program = False
        self.load_students()
        while  not exit_program:
            print("Welcome to the Student Management System!!")
            user_choice = input("Enter '1' to Add Student\nEnter '2' to search the Student\nEnter '3' to Update Student Details\nEnter '4' to Delete Student\nEnter '5' to Display all the Students\nEnter '6' to Exit\n")
            if user_choice == "1":
                name = input("Enter Name: ")
                try:
                    reg_no = int(input("Enter Reg_No: "))
                except ValueError:
                    print("Invalid input give only numbers.")
                    continue
                class_name= input("Enter Class: ")
                try:
                    marks= int(input("Enter Marks: "))
                except ValueError:
                    print("Invalid input.")
                    continue
                student = Student(name, reg_no,class_name,marks)
                self.add_student(student)
                self.save_students()
            elif user_choice == "2":
                self.search_student()
            elif user_choice == "3":
                self.update_details()
                self.save_students()
            elif user_choice == "4":
                self.delete_student()
                self.save_students()
            elif user_choice == "5":
                self.display_students()
            elif user_choice == "6":
                print("Exiting the program.")
                exit_program = True
            else:
                print("Invalid choice. Please try again.")
        print("Thank you for using the Student Management System!")
            
            
            


sms = StudentManagementSystem()

sms.system_menu()
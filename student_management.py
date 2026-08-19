from student import Student
import json
class StudentManagement:
    
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
            return False
        
                    
        for student in self.students:
            if student.reg_no == user_input:
                student.display()
                field = input("What do you want to update""\n(name, class_name, marks): ").lower()
                if field == "marks":
                    try:
                        new_value = int(input("Enter new value : "))
                    except ValueError:
                        print("Invalid input give only numbers.")
                        return False

                else :
                    new_value = input("Enter new value: ")  

                if hasattr(student,field):
                    setattr(student,field,new_value)
                    student.display()
                    print("student details is updated successfully")
                    return True
                else:
                    print("Invalid field name.")
                return False
        print("student not found") 
        return False

    def delete_student(self):
        try:
            user_input = int(input("Enter the Reg_no of the student to be deleted: "))
        except ValueError:
            print("Invalid input give only numbers.")
            return False
        
        
        for student in self.students:
            if student.reg_no == user_input:
                student.display()
                choice = input("Enter 'yes' to confirm or 'no' to stop : ").lower()
                if choice == "yes":
                    self.students.remove(student)
                    print("Successfully deleted the student")
                    return True
                elif choice == "no":
                    print("Deletion cancelled.")
                    return False
                else:
                    print("Invalid choice")
                    return False
                    
        else:

            print("Student not found")
            return False
 # Load student data from the file into the students list.
    def load_students(self):
        try:
            with open("students.json","r")as file:
                student_data = json.load(file)
                for json_dict in student_data:
                    student = Student(json_dict["name"],
                                       json_dict["reg_no"],
                                       json_dict["class_name"],
                                       json_dict["marks"])
                    self.students.append(student)
                print("Student data loaded successfully from the file.")
        except FileNotFoundError:
            print("No existing student data found. Starting with an empty list.")
        except Exception as e:
            print(f"Error while loading students: {e}")


# save student data from the students list to the file.
    def save_students(self):
        try:

            with open("students.json","w")as file:
                student_data = []
                for student in self.students:
                    json_student = {"name": student.name,
                               "reg_no": student.reg_no,
                               "class_name": student.class_name,
                               "marks": student.marks}
                    student_data.append(json_student)
                json.dump(student_data, file, indent =4)
                print("Student data saved successfully to the file.")    
        except Exception as e:
            print(f"Error while saving students: {e}")

        
    def system_menu(self):
        exit_program = False
        self.load_students()
        while not exit_program:
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
                result = self.update_details()
                if result:
                    self.save_students()
                else:
                    print("Update failed. Student not found or invalid input.")
            elif user_choice == "4":
                result = self.delete_student()
                if result:
                    self.save_students()
                else:
                    print("Deletion failed. Student not found or invalid input.")
            elif user_choice == "5":
                self.display_students()
            elif user_choice == "6":
                print("Exiting the program is set True.")
                exit_program = True
            else:
                print("Invalid choice. Please try again.")
        print("Thank you for using the Student Management System!")


            
 
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

student1 = Student("Raghav",101,"10th",75)
student2 = Student("Ramya",102,"10th",85)
student3 = Student("Laila",103,"10th",87)
student4 = Student("Raj", 104,"10th", 90)



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
        user_input = int(input("Enter the Reg_no of the student to search : "))
        for existing_student in self.students:
            if existing_student.reg_no == user_input:
                existing_student.display()
                return
        else:
            print("Student not found")

    def display_students(self):
        if not self.students:
            print("No student found !")
        for student in self.students:
            student.display()
            print("-" *30)

    def update_details(self):
        user_input = int(input("Enter the Reg_no of the student to update details : "))
        for student in self.students:
            if student.reg_no == user_input:
                student.display()
                field = input("What do you want to update""\n(name, class_name, marks): ").lower()
                if field == "marks":
                    new_value = int(input("Enter new value : "))
                else:
                    new_value = input("Enter new value: ")  

                if hasattr(student,field):
                    setattr(student,field,new_value)
                    student.display()
                    print("student details is updated successfully")
                else:
                    print("Invalid")
                return
        print("student not found")    

                



        


sms = StudentManagementSystem()
sms.add_student(student1)
sms.add_student(student2)
sms.add_student(student3)
sms.add_student(student4)
sms.update_details()
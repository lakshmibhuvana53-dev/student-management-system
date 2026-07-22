class Student:
    def __init__(self, name, class_name, roll_number, marks):
        
        self.name = name
        
        self.class_name = class_name
        
        self.roll_number = roll_number
        
        self.marks = marks
    
    def display(self):
        
        print(f"Name: {self.name}")

        print(f"Class: {self.class_name}")

        print(f"Roll Number: {self.roll_number}")

        print(f"Marks: {self.marks}")

student1 = Student("Alice", "10th Grade", 1, 85)

student2 = Student("Bob", "10th Grade", 2, 90)
class StudentManagementSystem:
    
    def __init__(self):
        
        self.students = []
    
    def add_student(self, student): 
        
        for existing_student in self.students:
            
            if student.roll_number == existing_student.roll_number:
                
                print(f"Student with roll number {student.roll_number} already exists.")
                
                return()
            
        self.students.append(student)

    def update_details(self):


        given_reg_no = int(input("Enter the roll number: "))

        for existing_student in self.students:

            if given_reg_no == existing_student.roll_number:

                field = input("What do you want to update?""\n(name/class_name/marks): ")
                

                new_value = input("Enter new value: ")

                if hasattr(existing_student, field):
                    setattr(existing_student, field, new_value)
                    print("Student updated successfully.")
                else:
                    print("Invalid field.")

                return

        print("Student not found.") 

    def search_student(self):
        
        given_reg_no = int(input("Enter the  roll_number of the student:  "))

        for existing_student in self.students:

            if given_reg_no == existing_student.roll_number:

                existing_student.display()

                return
        print("Student not found")

    def delete_student(self):

        given_reg_no = int(input("Enter the rol_number of the student: "))

        for existing_student in self.students:

            if given_reg_no == existing_student.roll_number:

                existing_student.display()

                field = input("Enter 'yes' to confirm or enter no: ").lower()

                print(field)

                if field == "yes":

                    delattr(existing_student,field)


                

sms = StudentManagementSystem()

sms.add_student(student1)

sms.add_student(student2)
 
student3 = Student("Charlie", "10th Grade", 3, 85)

sms.add_student(student3)

sms.delete_student()






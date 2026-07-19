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
student2 = Student("Bob", "11th Grade", 2, 90)
print("Student Information:")
student1.display()
student2.display()

class Studentmanagementsystem:
    def __init__(self):
        self.students = [student1, student2]
    def add_student(self, student): 
        self.students.append(student)
               


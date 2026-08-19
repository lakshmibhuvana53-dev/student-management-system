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


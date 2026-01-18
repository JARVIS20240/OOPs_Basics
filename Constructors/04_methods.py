# Methods are Functions that belongs to objects.
# Functions inside the class called Methods.
"""
Class has store two things 
1) Data (Attributes) = Which properties class have.
2) Methods = what can class do..
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student,",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("karan", 80)
s1.welcome()
print(s1.get_marks())
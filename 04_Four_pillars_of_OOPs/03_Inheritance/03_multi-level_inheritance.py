"""
Inheritance Type:
2).Multi-level Inheritance: A class is derived from another derived class (parent → child → grandchild).
"""

"""
+------------+
|  Base      |  (Parent)
+------------+
      ↓
+------------+
|  Derived   |  (Child-1,Parent for Child-2)
+------------+
      ↓
+----------------+
| Sub-Derived    |  (Child-2)
+----------------+

"""
class Cars: # Paren-1
    @staticmethod
    def start():
        return "Car Started..."
    
class ToyotaCar(Cars): # Child-1 (Parent for Child-2)
    @staticmethod
    def stop():
        return "Car Stopped..."

class Fortuner(ToyotaCar): # Child-2
    def  __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")

print(car1.type)
print(car1.start())
print(car1.stop())

# Scenario: A CollegeStudent is a Student, and a Student is a Person.
class Person:
    def info(self):
        return "I am a Person."

class Student(Person):
    def study(self):
        return "I am a Student."

class CollageStudent(Student):
    def collage(self):
        return "I study in Collage."
    
std1 = CollageStudent()
print(std1.info())
print(std1.study())
print(std1.collage())
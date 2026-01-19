
class Student:
    # Default Constructor...
    def __init__ (self):
            pass

    #Parameterized canstructor...
    def __init__ (self, name, marks): #<-- self = s1 object it self. & name = perameters
        self.name = name #<-- it means indirectly we say s1.name = name
        self.marks = marks
        print("Adding a new student in database...")

s1 = Student("Karan", 93)
s2 = Student("Arjun", 90)

print(f"Student name '{s1.name}', has {s1.marks} Marks in Python Fundamentals Test.")
print(f"Student name '{s2.name}', has {s2.marks} Marks in Python Fundamentals Test.")

# When we code s1 = Student("karan", 30) Python looks that like --> Student.__init__(s1,"karan", 30) 

"""
Notes:

in this class...
(self, name, marks) --> called Parameters of Function, But Self is not a normal Parameter
self --> called Referanced of Current Object (Here's s1)
.name, .marks --> Called attributes (Instance variable) of objcet s1
('karan', 30) --> Called Arguments of Parameters 
"""

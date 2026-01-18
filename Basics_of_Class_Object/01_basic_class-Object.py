#Class is a Blueprint for creating object.
"""
        ---------
        | Class |
        ---------
            |
     -----------------
     |               |
  -------         -------
  | OBJ |         | OBJ |
  -------         -------

"""
#class:
class Student:
    name = 'Karan' #<-- Default name of every Object 

s1 = Student() #<-- It's Called Class Object (Instance)
print(f"Student-1 Name: {s1.name}")

s2 = Student()
print(f"Student-2 Name: {s2.name}")

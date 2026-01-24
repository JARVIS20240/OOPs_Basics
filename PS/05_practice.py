"""
Practice: 
1. Create a Class “Programmer” for storing information is few programmers
    working at Microsist.
2. Write a class “calculator” capable is finding square, cube and square root is a
    number.
3. Create a class with a class attribute a; create an object from it and set 'a'
    directly using object.a = o. Does this change the class attribute?
"""

# Problame: 01
class Programmer:
    Company = "Microsist"

    def __init__(self, name, roal, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        self.roal = roal
        return print(f"{self.Company} Programmer Name: {self.name} Good at {self.language} Language, working at {self.roal} at {self.salary} Salary. ")

emp1 = Programmer("Karan", "AI/Ml Developer", "Python", 1500000)

# Problame: 02
class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        return print(f"Square is {self.num ** 2}")

    def quabe(self):
        return print(f"Quabe is {self.num ** 3}")
    
    def square_root(self):#*1/2
        return print(f"Square root is {self.num ** 0.5}")

num1= Calculator(4)
num1.square()
num1.quabe()
num1.square_root()

# Problame: 03
class data:
    a = 1

obj1 = data()
obj1.a = 0
print(obj1.a, data.a)
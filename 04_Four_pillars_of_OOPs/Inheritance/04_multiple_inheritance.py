"""
Inheritance Type:
3).Multiple Inheritance: One child class inherits from more than one parent class..
"""

"""
        Parent Class
+--------+     +--------+
| Base A |     | Base B |
+--------+     +--------+
      \           /
       \         /
        ↓       ↓
        +---------+
        | Derived |
        +---------+
        Child Class
"""
class A: # Parent A
    varA = "Welcome to calss A."

class B: # Parent B
    varB = "Welcome to calss B."

class C(A, B): # Child of A & B
    varC = "Welcome to calss C."

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# Scenario: A Student is both a Person and a Player.
class Player:
    def sport(self):
        return "I am Cricket player."
    
class Person:
    def info(self):
        return "I am Student of ABC Collage."

class Student(Person, Player):
    pass

std1 = Student()
print(std1.info())
print(std1.sport())
"""
Inheritance Types:
1).Single Inheritance: Single Base (parent) class and single Drived (Child) Class.
OR 
One child class inherits from one parent class.
"""

"""
+--------+
|  Base  | (Single Parent)
+--------+
     ↓
+---------+
| Derived | (Single Child)
+---------+

"""

# Single Inheritance:
class parent:
    
    @staticmethod
    def hello():
        return "Hello.!"
    
    @staticmethod
    def welcome():
        return "welcome.!"

class child(parent) :
    def __init__(self, name):
        self.name = name

ch1 = child("jhon")
print(ch1.name)
print(ch1.hello(),ch1.welcome()) #This Gives Error Bec... ch1 has no attribute name hello()
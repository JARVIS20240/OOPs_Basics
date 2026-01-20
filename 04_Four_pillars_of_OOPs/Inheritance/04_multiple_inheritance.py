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
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

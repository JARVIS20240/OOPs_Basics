"""@property decorator lets you access a method like an attribute, while still running code behind the scenes."""
class Student:
    def __init__(self,math,phy,chem):
        self.math = math
        self.phy = phy
        self.chem = chem

    @property #Use Method Like Objcet/instance Property 
    def percentage(self):
        return str((self.math + self.chem + self.phy)/3) + "%"

s1 = Student(70,80,90)

print(s1.percentage)

# marks change
s1.math = 80
s1.chem=100
print(s1.percentage)

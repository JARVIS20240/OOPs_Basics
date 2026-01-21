"""@property decorator lets you access a method like an attribute, while still running code behind the scenes."""
class Student:
    def __init__(self,math,phy,chem):
        self.math = math
        self.phy = phy
        self.chem = chem

    # def cal_percentage(self):
    #     self.percentage = str((self.math + self.chem + self.phy)/3) + "%"
    @property
    def percentage(self):
        return str((self.math + self.chem + self.phy)/3) + "%"

s1 = Student(70,80,90)

# marks change
s1.math = 80
s1.chem=100
print(s1.percentage)

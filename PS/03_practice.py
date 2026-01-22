"""
Qs. Define a Circle class to create a circle with radius r using the constructor.
    Define an Area() method of the class which calculates the area of the circle.
    Define a Perimeter() method of the class which allows you to calculate the perimeter of the
    circle.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        # A = Pi * (r*r)
        Area = 3.14 * (self.radius * self.radius)
        # return 3.14 * self.radius ** 2
        return print(f"Area of Circle: {Area}")

    def Perameter(self):
        # P = (2*Pi) * r
        Perameter = (2 * 3.14) * self.radius
        # return 2 * 3.14 * self.radius
        return print(f"Perameter of Circle: {Perameter}")

c1 = Circle(21)
print(c1.radius)
c1.Area()
c1.Perameter()
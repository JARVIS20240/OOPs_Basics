"""
Static Methos:
Till now we use

average(), __init__() methods are Not-Static methods, normal methods that use Self parameters.
But
static method not need to get self parameters.

STATIC METHODS works on "CLASS-LEVEL"
"""

class Student:

    @staticmethod   #used for create Static method 
                    # @staticmethod Called Dacorator
    def hello():
        print("hello")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value

        print(f"{self.name},\nYour avg score is: {sum / len(self.marks)}")

s1 = Student("Tony stark", [10,20,30,40])
s1.hello()
s1.get_average()

"""
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the get_average.
"""
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value

        print(f"Hi {self.name}, your avg score is: {sum / len(self.marks)}")

s1 = Student("Tony stark", [10,20,30,40])
s1.get_average()

s1.name = "Ironman"
s1.get_average()
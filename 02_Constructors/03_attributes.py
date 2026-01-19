"""
Two Types of Attrbutes:
1) Class attr. --> Common for all objects.
2) Instance/Object attr. -->diffener data for each Objects/Instances.
"""

class Student:
    college_name = "ABC College" #<-- Class Attribute
    # name = "Anonymous"

    def __init__(self, name):
        self.name = name #<-- objcet/Instance Attribute
        # Objcet Attr. > Class Attr.


s1 = Student("karan")

print(f"'{s1.name}' is student of '{Student.college_name}'")

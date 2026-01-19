'''
Del Keyword:
--> Used for delete Object properties or Object it self
'''

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Karan")
print(s1)
print(s1.name)

print("Delete Object (s1) properties (.name): ")
del s1.name

print("Delete Object (s1):")
del s1

# print(s1) #Give NameError : s1 not defined
# print(s1.name) 

'''
Private attributes and methods are restricted to the class and cannot be used outside the class.
'''
# Private attributes and methods are created by adding "Double Underscores" = (__) before their name, so they can be used only inside the class.

class Person :
    __name = "karan" # private attribute

    def __hello(self): # private Method
        print("Hello person!")
    
    def welcome(self):
        self.__hello()

p1= Person()

print(p1.welcome())
# print(p1.__name) #❌ Error
# print(p1.__hello()) #❌ Error

# -----------------------------------------------------------------------------------------------
class Account:

    def __init__(self, acc_no, acc_pass):
        self.__acc_no = acc_no # private attribute
        self.__acc_pass = acc_pass # private attribute

    def __info(self): # private Method
        return f"Display:\nAccount No: {self.__acc_no}\nAccount password: {self.__acc_pass}\nInside Calling method" # allowed inside the class                                                 

    def display(self):
        return self.__info() # allowed inside the class

u1 = Account("123789", "Admin@123")
# print(u1.__acc_no, u1.__acc_pass) #❌ Error Outside class
# print(u1.__info) #❌ Error
print(u1.display())

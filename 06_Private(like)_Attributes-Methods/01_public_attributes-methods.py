'''
Public attributes and methods are accessible from any part of the program, both inside and outside the class, and form the external interface of an object.
'''

class Account:
    def __init__(self, acc_no, acc_pass): #public method 
        self.acc_no = acc_no
        self.acc_pass = acc_pass

    def name(self, name ): #public method 
        self.name = name
        return f"User name: {self.name}"

user1 = Account("123456", "admin@123")

print(user1.name("Karan")) # accessible outside the class

print(f"Acc No: {user1.acc_no}") # accessible outside the class
print(f"Acc Pass: {user1.acc_pass}") # accessible outside the class
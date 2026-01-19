# Inheritance :
'''one class uses the properties and methods of another class.'''

# Without Inheritance:
class parent:
    @staticmethod
    def hello():
        print("Hello.!")
    
    @staticmethod
    def welcome():
        print("welcome.!")

class child :
    def __init__(self, name):
        self.name = name

ch1 = child("jhon")
print(ch1.name)
# print(ch1.hello()) #This Gives Error Bec... 

# With Inheritance:
class Cars: # Parent Class
    @staticmethod
    def start():
        return "Car Started..."
    
    @staticmethod
    def stop():
        return "Car Stopped..."

class ToyotaCar(Cars): # ToyotaCar is a Child Class of Parent class (Cars)
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.name)
print(car1.start()) #If there is No inheritance we do there is an error
print(car1.stop())
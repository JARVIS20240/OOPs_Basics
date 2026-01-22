# Abstraction:
'''Abstraction is the process of hiding internal implementation details and showing only essential features to the user.'''

# Encapsulation:
'''Wrapping data and Functions into a single unit (object).'''
class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started....")

car1= Car()
car1.start()
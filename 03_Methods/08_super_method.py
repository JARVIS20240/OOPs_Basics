"""
Super methd: super() method is used to access methods of the parent class. 
"""
class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")
    
class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        # super().stop()

car1 = ToyotaCar("Fortuner", "electric")
print(car1.type)
# print(car1.stop())
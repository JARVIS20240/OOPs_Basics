"""Polymorphism :Polymorphism in Python means the same method name can have different behaviors depending on the object calling it."""

"hear a same operator '+' have diff behaviors according data type. it's called 'Operator Overloading'."
# print(1+3) #3
# print("Hello " + "Karan") #concatenate
# print([1,2,3] + [4,5,6]) #merge

"""
Polymorphism: Operator Overloading
When the same operator is allowed to have different meaning according to the context.
Operators & Dunder functions
  a + b #addition a._ _ add __( b )
  a-b #subtraction a. _ sub __( b )
  a*b #multiplication a._ _ mul _ _ _ __( b )
  a/b #division a.__ truediv ___( b )
  a % b #addition a.__ mod ____( b )
"""
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img                                 

    def showNumber(self):
        print(self.real,"i +", self.img,"j")
        
    def _add_(self, num2):
        newReal = self.real + num2. real
        newImg = self.img + num2.img
        return Complex (newReal, newImg)
    
    def _sub_(self, num2):
        newReal = self. real - num2. real
        newImg = self.img - num2.img
        return Complex (newReal, newImg)
    
num1 = Complex (1, 3)
num1.showNumber()

num2 = Complex (4, 6)
num2.showNumber()
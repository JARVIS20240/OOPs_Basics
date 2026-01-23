class car:
    color = 'Blue' #This is a Class Attribute
    brand = "mercedes"

car1 = car()

print(f"My 1st car color is {car1.color} and it's {car1.brand} brand")

class Employee:
    language = "Py"
    salary = 1200000

e1 = Employee()
e1.name = "Karan" ##This is a Object/Instance Attribute
print(f"Name: {e1.name}\nSalary: {e1.salary}\nlanguage: {e1.language}")
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


class Engineer(Employee):
    def __init__(self, name, age, roal, department, salary):
        self.name = name
        self.age = age
        super().__init__(roal, department, salary)
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        return super().show_details()


e1 = Engineer("Karan M", 21, "Python Engineer", "IT", 75000)
e1.show_details()

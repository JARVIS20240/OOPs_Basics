class Employee:
    language = "Python"
    salary = 1200000

e1 = Employee()
e2 = Employee()
print(f"{e1.language}\n{e2.language}")
e2.language = "JavaScript"
print("\nInstance Attribute taks prefrances over the Class Attributes during the assignment and retrival.")
print("\n(Instance Attributes > Class Attributes):")
print(f"{e1.language}\n{e2.language}")
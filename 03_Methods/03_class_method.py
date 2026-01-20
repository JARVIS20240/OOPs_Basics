class person:
    name = "Unknown"

    def __init__(self, name):
        self.name = name

p1 = person('karan')
print(p1.name)
print(person.name)
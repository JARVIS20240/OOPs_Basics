"""
Class Method :
with the help of class method we can read or modify class level data that is shared by all object.
"""
# Normal way to change Class Attribute.
# Not change:
class person:
    name = "Unknown"

    def changename(self, name):
        self.name = name

p1 = person()
p1.changename("karan")
print(p1.name)
print(person.name)

# Change:
class user :
    name = "Unknbown"

    def changeN(self, name):
        user.name = name
        # self.__class__.name = name
u1 = user()
u1.changeN("karan")
print(u1.name)
print(user.name)

# change with Class method:
"""
Syntex:
    class person:
        @classmethod
        def changeName(cls):
            pass
"""
class user_data:
    name = "Not_defined"

    @classmethod
    def chnage(cls, name):
        cls.name=name

ud1 = user_data()
print(ud1.name)
ud1.chnage("Karan_Mistr") #Chnage Not_Defined Class Attribute Value
print(ud1.name)
print(user_data.name)
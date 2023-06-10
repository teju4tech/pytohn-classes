# This is Parents class 
class Employee:
    a = 45
# This is child class
class Programmer(Employee):
    b = 56

# we can Inherite the property of an class
pr = Programmer()
print(pr.a)
print(pr.b)

# This can have only Parents Property
Em = Employee()
print(Em.a)
# print(Em.b)
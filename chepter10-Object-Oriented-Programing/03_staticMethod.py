''' Static method are does't requered any object '''

# Class define
class Employee:
    Name = 'Tejpal singh'
    Sallary = 30000
    UIDno = 12345
    Branch = 'Devlopment Operations'

    # Normal methods 
    def printObj(self):
        print(f"Mr. and Mis.is {self.Name}")
        

    # Static method
    @staticmethod
    def greet():
        print("Good day")

    
Employee.Name = "ishpal"
info = Employee()
jankari = Employee()
jankari.Name = 'Tejpal singh'#Instent attribute
print(info.Name)
# print(info.Branch)
print(jankari.UIDno)
print(jankari.Name)
info.printObj() #Employee.printobj(info)
Employee.printObj(info) 
''' Static method'''
info.greet()
Employee.greet()


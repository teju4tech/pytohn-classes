''' Class method '''

class Employee:
    Name = 'ishika Rathore'#class attribute
    Sallary = 10000
    UIDno = 123145
    Branch = 'Product shipping'
 
    def printobj(self):
        print(f"The name is {self.Name}")

info = Employee()
jankari = Employee()
jankari.Name = 'Tejpal singh'#Instent attribute
# print(info.Name)
# print(info.Branch)
print(jankari.UIDno)
print(jankari.Name)
info.printobj()


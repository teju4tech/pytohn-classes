'''If you want to do mathemeticle operations
   use dunderMethod add 
'''
class Employee:
    def __init__(self,a):
        self.a = a
    '''ADD METHOD'''
    def __add__(self,obj):
        return self.a + obj.a
    '''SUBSTRACT METHOD'''
    def __sub__(self,obj):
        return self.a - obj.a
    '''MULTIPLICATION'''
    def __mul__(self,obj):
        return self.a * obj.a
    '''DIVITION'''
    def __truediv__(self,obj):
        return self.a / obj.a
    '''FLOORDIVITION'''
    def __floordiv(self,obj):
        return self.a // obj.a

           
a = Employee(45)
b = Employee(40)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)

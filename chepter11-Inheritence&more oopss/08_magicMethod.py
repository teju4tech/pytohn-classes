''' Here's some magic method's '''
class Employee:
    def __init__(self,a,name):
        self.a = a
        self.name = name
    
    def __add__(obj):
        return self.a + obj.a
    
    def __str__(self):
        return self.name

    ''' If we don't have str 
        method The output is this
       <__main__.Employee object at
        0x0069DD30> <__main__.Employee
        object at 0x006AF6F0>
    '''
    def __len__(self):
        return self.a
    ''' This will return the int 
        of atrribute
    '''

a = Employee(2,'Teju')
b = Employee(3,'Ishu')

print(a , b)
# print(a + b)
print(len(a))
print(len(b))
    


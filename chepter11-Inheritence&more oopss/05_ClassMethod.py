class Employee:
    a = 40
    b = 80
    c = 60
    #ClassMethod
    @classmethod
    def setAttribute(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c

emp  = Employee()
print(emp.a)
print(emp.b)
print(emp.c)
print("\n")
emp.setAttribute(1,2,3)
print(emp.a)
print(emp.b)
print(emp.c)   
    
    


    

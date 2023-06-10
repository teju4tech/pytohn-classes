class Employee:
    a = 10
    b = 20
    c = 30

    @classmethod
    def setAttribute(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c 

    @property
    def length(self):
        return self.a
    ''' Setter'''
    @length.setter
    def length(self,value):
        self.a = value

    
emp = Employee()
emp.setAttribute(1,2,3)
emp.length = 56
print(emp.length)

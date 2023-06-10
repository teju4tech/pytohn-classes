'''a class complex to represent complex numbers,
   along with overloaded operators + and * which
   adds and multipily? 
'''
'''MI Solution'''
class comPlex:
    def __init__(self,a):
        self.a = a
    
    def __add__(self,obj):
        return self.a + obj.a

    def __mul__(self,obj):
        return self.a * obj.a
    

a = comPlex(45)
b = comPlex(67)

print(a + b)
print(a * b)
print("---Next-----------")

'''Mentor's solution'''
'''Complex Number - Fist part will be 
   real and sec term is imagenery.
'''
class Complx:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self,obj):
        return Complx(self.a + obj.a,self.b + obj.b)
    
    def __mul__(self,obj):
        return Complx(self.a *obj.a,self.b * obj.a)

c1 = Complx(1,2)
c2 = Complx(4,7)
c3 = (c1+c2)
print(c3.a + c3.b)
c3 = (c1*c2)
print(c3.a * c3.b)
'''a class vector representing a vector
   of n dimension Overload the + and *
   operator which calculates the sum 
   and the dot product of them...?
'''
'''MI Solution'''
class Vector:
    def __init__(self,i,j):
        self.i = i 
        self.j = j 
    
    def printObj(self):
        print(f"{self.i} i + {self.j} j")
    
    # Implementing Methods
    def __add__(self,obj):
        return Vector(self.i + obj.i,self.j + obj.j)

    def __mul__(self,obj):
        return Vector(self.i * obj.i,self.j + obj.j)
    
class vector2D(Vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    
    def printObj2(self):
        print(f"{self.i} ^i + {self.j} ^j + {self.k} ^k")

print("---Nakli kaam Hai----")
v1 = Vector(12,14)
v2 = vector2D(45,78,67)
v1.printObj()
v2.printObj2() 

print("-----Asli Kaam hai Bhai----")
d1 = Vector(1,4)
d2 = Vector(6,7)
d3 =(d1+d2)
print(d3.i + d3.j)
print(d3.i * d3.j)


'''Mentor's Solution'''


    

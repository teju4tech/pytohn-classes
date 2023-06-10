'''OverRide the __len__() method on Vector of
   problem 5 to display the dimentions of the
   Vector.
'''
'''MI Solution'''
# class Vector:
#     def __init__(self,i,j,k,name):
#         self.i = i
#         self.j = j
#         self.k = k
#         self.name = name
    
#     def __str__(self):
#         return f"{self.i}^I + {self.j}^J + {self.k}^k+{self.name}"

#     def __len__(self):
#         return self.i 
# v = Vector(2,56,23,'Teju')
# print(v)
# print(len(v))

'''Mentor's Solution''' 
'''This Q is going to Crezy bcz We need list and
   addding li2 to li1 by one by one !!!
'''
class Vender:
    def __init__(self,l1):
        self.dim = len(l1)
        self.data = l1

    def __add__(self,obj):
        myList = []
        for i in range(len(obj.data)):
            myList.append(obj.data[i]+self.data[i])
        return Vender(myList)
    
    def __mul__(self,obj):
        dot = 0
        for i in range(len(obj.data)):
            dot += (obj.data[i]*self.data[i])
        return dot
    
    def __len__(self):
        return len(self.data)

    
v1 = Vender([45,56,78])
v2 = Vender([6,8,4])
'''v3 = [51,64,82] = [45+6,56+8,78+4]'''
v3 = v1 + v2
v4 = v1*v2 #V4 is a scaler not a vector
print(v3.data)
print(v4)
'''v4 = 1030 = v1xv2 = 45x6+56x8+78x4'''
print(len(v3))


    

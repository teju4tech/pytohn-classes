'''Q1]crete a class Ec2vector and use it to
   create another class representing a 3D 
   vector ?
'''
'''Mi solution'''
class Ec2vector:
    def __init__(self,Name):
        self.Name = Name
        super().__init__()
    
class D3Dcalss(Ec2vector):
    def __init__(self,vector):
        for i in range(j):
            for j in range(i):
                print('Vec')
    
# ec2 = Ec2vector()
# ec2.Name = 'Teju'
# d3d = D3Dcalss()
# print(d3d.vector)
# print(ec2.Name)

'''Mentor's solution'''
class vector2D:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def print2dvector(self):
        print(f"{self.i}i + {self.j}J")

class vector3D(vector2D):
    def __init__(self,i,j,k):
        '''self.i = i
           self.j = j
        '''
        #DRY-Don't Reapeat yourself
        #For ignoring these repeating we will use super key word
        super().__init__(i,j)
        self.k = k
    
    def print3dvector(self):
        print(f"{self.i}i + {self.j}j +{self.k}k")

    
v2 = vector2D(1,5)
v3 = vector3D(1,6,8)

v2.print2dvector()
v3.print3dvector()










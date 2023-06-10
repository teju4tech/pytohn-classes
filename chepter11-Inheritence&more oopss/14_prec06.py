''' __str__ method to print the vector as follows
    7^i + 8^j 10^k
'''
'''MI Solution'''
# class Vector:
#     def __init__(self,i,j,k):
#         self.i = i 
#         self.j = j
#         self.k = k
#         # self.name = name
    
#     # def __str__(self):
#     #     return self.name
    
#     # def __str__(self):
#     #     return  f"{self.i} ^i + {self.j} ^j + {self.k} ^k"
    

# V = Vector(45,67,12)

class Raw:
    def __init__(self,i,j,k):
        self.i = i 
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v = Raw(56,78,34)
print(v)
'''Mentor's Solution'''


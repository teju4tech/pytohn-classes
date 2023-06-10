''' creat a class atrribute a,
    creat a object from it and set directly 
    using a = 0 Does this change the class arribute ?
'''
#MY APROOCH
class A:
    def __init__(self,a):
        self.a = a 

    @staticmethod
    def greet():
        print('Good Morning')
    
    def printObj(self):
        print(f"This is Power of {a}")
    
# creating object     
# a = A()
# Creating atrribute for a
# a = "Dalla"
# a.printObj()

class MuClass:
    a = 9

obj = MuClass()
print(obj.a)
obj.a = 0 #INstence attribute not 
print(obj.a)
print(MuClass.a)


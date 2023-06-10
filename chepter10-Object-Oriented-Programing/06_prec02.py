'''Make a class for calculater for calculating 
   square cube and sqare root?
   Khud se banaya
'''
import math
class Calculater:
    def __init__(self,N):
        self.N = N
    
    def FullCal(self):
        print(f"This is Number is: {self.N}")
        print(f"This is The Squre is:{self.N*self.N}")
        print(f"This is The Squre is:{self.N*self.N*self.N}")
        print(f"This is The SqureRoot is: {math.sqrt(self.N)}")

    @staticmethod
    def greet():
        print('HApy Coding')

N = int(input("Enter the Number: "))
Cal = Calculater(N)
Cal.FullCal()
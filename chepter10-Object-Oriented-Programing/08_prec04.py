''' Add static mehod on prec 02'''
''' Actully we only print Good moring
    but i was getting more excited !!!
'''
import math
class Calculater:
    # def __init__(self,Number):
    #     self.Number = Number
    
    @staticmethod
    def printObj(self,Number):
        print(f"The Square is :{self.Number*self.Number} ")
        print(f"The Cube is: {self.Number*self.Number*self.Number}")
        print(f"The sqaureRoot is: {math.sqrt(self.Number)}")

cal.printObj(7)


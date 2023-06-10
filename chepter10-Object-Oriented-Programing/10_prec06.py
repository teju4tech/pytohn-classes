'''can you change the self parameter inside
   a class to something else (say 'babu') try 'slf'
   and 'teju'?
'''
class stuDent:
    def __init__(self,Number):
        self.Number = Number

    def printObj(slf):
        print(f"This is the number: {slf.Number}")
    @staticmethod
    
    def greeting():
        print('Good Morning')
    
'''we can change self with anything'''
'''This can not harm our program'''
'''The Effect was  reduce readability of our program'''

Numeric = stuDent(5)
Numeric.printObj()
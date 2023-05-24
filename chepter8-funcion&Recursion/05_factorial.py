''' Factoraial(n) = n * Factoraial(n-1)
     factorial (4) = 4 x 3 x 2 x 1
     factorial (0) = 1(By defination)
'''
def factorial(n):
     #Base condition
     if(n==0 or n==1):
         return 1
     return n * factorial(n-1)

A = factorial(5)
print(A)  
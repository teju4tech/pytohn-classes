# Q- Recursive funcion to calculate the sum of first n natural numbers?

def SumOFN(n):
    #Base condition
    if(n==1 or n==0):
        return 1
    #Main conditions
    return n + SumOFN(n-1)

A = SumOFN(5)
'''5 = 5+4+3+2+1 = 15 '''
print(A)


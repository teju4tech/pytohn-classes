'''Q-pattern using recursion
   *
   * * 
   * * * 
'''
def  pattern(n):
     #base condition
     #main condition
     for i in range(n):
         print(n-i)

# A = pattern(5)
# print(A)

def printpat(n):
    for i in range(n):
        print("*"*(n-i))
    
A = printpat(6)
# print(A)

def printpat1(n):
    for i in range(n):
        print("*"*(n+i))

printpat1(5)
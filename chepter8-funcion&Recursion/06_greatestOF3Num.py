# Q- find greatest of three num using recursion?
# def greatest(a,b,c):
#     if(a>b or a>c):
#         print(f"{a} is greatest")
#     elif(b>a or b>c):
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greator")

# A = greatest(1,2,3)
# print(A)

def great(n1,n2,n3):
    if(n1>n2):
        greater = n1
    else:
        greater = n2
    if(n3>greater):
        greater = n3
    return greater

a = great(1,34,12)
print(a)





''' A list comprehension to print a list which contains 
    the multiplication table of a user enetered number?
'''
'''MI Solution'''
# a = int(input("Enter a:"))
# l1 = []
# for i in range(1,11):
#        A = a*i
#        print(A)
#        l1.append(A[i])
    
# print(l1)

'''Mentor's Solution'''
num = int(input("Enter the number: "))
multiplication = [i*num for i in range(1,11)]
print(multiplication)


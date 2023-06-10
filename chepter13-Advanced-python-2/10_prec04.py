'''A program to filter a list of number which
   are divisible by 5 ?
'''
'''MI solution'''

divi = lambda x:x%5==0
li = [i*9 for i in range(1,11)]
# li = [1,2,3,4,5,6,7,8,9,10]
print(li)
D = filter(divi,li)
print(list(D))

'''Mentor's Solution'''
def is_divisible(n):
    if n%5 ==0:
        return True
    return False
a = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(is_divisible,a)))

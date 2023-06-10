'''To find the maximum of the numbers in a list using
   the reduce function?
'''
'''MI Solution'''
from functools import reduce

def gretor(c,d):
    if c>d:
        return c
    return d 
li = [i*6 for i in range(1,11)]
print(li)
st = ''
for item in li:
    st += str(item) + '\n'
print(st)
R = reduce(gretor,li)
print(R)

'''Mentor's Solution'''
def max(m,n):
    if m>n:
        return m
    return n 
a = [1,23,122,223,500]
maxNum = reduce(max,a)
print(a)
print(maxNum)
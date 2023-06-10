'''[Map function]-Map applies a function to all the
                  items in an input_list.
'''
square = lambda x:x*x
l1 = [1,2,3,4,5,6]
mp = map(square,l1)
print(list(mp))#Type casting to a  list

'''[filter function]-Filter applies a function to all
                     the input items list
'''
gretor = lambda x:x>4
a = [1,2,3,4,34,21,23,67,78]
d = filter(gretor,a)
print(list(d))

'''[Reduse fuction]-Reduse applies a rolling computation
   to sequential pair of elements
   list = [1,2,3,4]
   Reduse works like:
     Reduse(1,2)->|1+2| = 3
     Reduse(2,3)->|3+3| = 6
     Reduse(3,4)->|6+4| = 10
'''
from functools import reduce
sum = lambda x,y:x+y
lis2 = [1,2,3,4]
D = reduce(sum,lis2)
print(D)
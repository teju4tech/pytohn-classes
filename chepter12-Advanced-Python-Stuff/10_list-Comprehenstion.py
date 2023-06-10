'''We want to make a list2 from lis1 
  first method is to use loop
  and second is to use brains
'''
l1 = [1,4,5,2,7,8]
# l2 = []
# for item in l1:
#     l2.append(item*(item))
l2 = [i*i for i in l1 if i>2]
l4 = [i*i for i in l1 ]
print(l1)
print(l2)
print(l4)
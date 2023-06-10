'''A program to print 3rd,5th,and 7th element
   from a list using enumerate function ?
'''
'''MI code Solution'''
l1 = [1,2,3,4,5,6,7]
# l1 = [12,11,22,14,23,56,67]
l2 = []
# i = 0
# for item in l1:
#     if(item>4):
#         l2.append(item)
'''Using enumeration method'''
l2 = [i for i in l1 if i>4 ]
print(l2)

'''Mentor's Solution'''
list1 = [1,2,3,4,5,6,7,8,9,10]
for index, item in enumerate(list1):
   if(index+1==3 or index+1 == 5 or index == 7):
      print(item)
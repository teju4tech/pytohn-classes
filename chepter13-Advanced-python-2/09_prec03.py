'''A list contains the multiplication table of 7.
   Write a program to Canvert it to a Verticle
   String of same Numbers(7,14) ?
'''
'''MI Solution'''
li = [i*7 for i in range(1,11)]
st = ""
print(li)
for item in li:
   st += str(item) + '\n'
print(st)

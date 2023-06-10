''' we can change global variable in python 
    using global keywords
'''
a = 9#global keywords
def fun():
    global a # this will modified global variable a =1000
    a = 8
    print(a)#personal
    a = 1000#overWrited
    print(a)
print(a)
fun()
# 9 was global
print(a)
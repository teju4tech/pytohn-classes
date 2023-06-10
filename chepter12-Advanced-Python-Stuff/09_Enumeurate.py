'''When we are do some increment or dicrement or 
   something we need a loop and then iterate something
   but the Easiest way is Enumerate that
'''
a = [1,2,67,'apple']
# i = 0
# for item in a:
#     print(f"Item number {i} is {item}")
#     i += 1
for i,item in enumerate(a):
    print(f"Item number {i} is {item}")
'''Now starts from 1 not 0'''
print("\n\n")
for i,item in enumerate(a):
    print(f"Item number {i+1} is {item}")   
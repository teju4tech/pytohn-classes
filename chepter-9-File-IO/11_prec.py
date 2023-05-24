'''Check whether is file' data  is same or not '''

with open("copy.py","r") as f:
    A = f.read()

with open("write.txt","r") as f1:
    B = f1.read()

if(A==B):
    print(f"data is same \n")
    print(f"data is same\n")

else:
    print(f"{A}\n\n\n is different with\n\n{B}")
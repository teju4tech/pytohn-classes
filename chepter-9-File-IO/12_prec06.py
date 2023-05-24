''' Change any file's Extention using python '''

import os

oldname = input("Enter the oldfname:")
newname = input("Enter the Newname: ")

with open(oldname,"r") as f:
    text = f.read()

with open(newname,"w") as f:
    f.write(text)

# os.remove(oldname)
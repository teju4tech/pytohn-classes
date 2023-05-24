'''Make file copy to another file'''
import os
with open("write.txt","r") as f:
    text = f.read()

with open("copy.py","w") as f:
    txt = f.write(text)
os.system("python")
os.system("color 0a")

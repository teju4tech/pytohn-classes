'''Q-A program to make to find 
   another file Is containing 
   Twencle word or not
'''
with open("mine.txt","r") as f:
    if('Twencle' in f.read()):
        print("yes Twencle is present")
    else:
        print("NO Twencle is here babe")
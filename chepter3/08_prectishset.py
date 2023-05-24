#write a program to fill in a letter templete Given below with name and date
#Letter=
# " < Name> You'r selected ! <date>"
import os
Name = input("Enter you'r name: ")
print(Name + "You'r selected !")
date = os.system("date")

#youtuber tric
name = input("Enter the name: ")
date = input("Enter the date: ")
templete=  ''' 
dear <|name|>,
you'r selected !!
<|date|>
'''
print(templete.replace('<|name|>',name).replace('<|date|>',date))


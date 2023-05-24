'''Q- A file contains a word "donkey"
 mulfiple need to write a program which
 replace with Raja by updating the same file?
'''

with open("mine.txt","r") as f:
    text = f.read()

text = text.replace("donkey","Raja")

with open("mine.txt","w") as f:
    f.write(text)
    

    
    

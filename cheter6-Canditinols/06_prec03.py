# Q-Make a program to detect spam in mail 
# "Make a lot of money" "bay now" "subscribe this "
# "click this " "Course" "Discount"

# make list of all these of words
spamWords = ['buy now','subscribe now','click this','a lot of money']
email = input("Enter the massage: ").lower()
spam = False

if('buy now' in email):
    spam = True
if('money' in email):
    spam = True
if('subscribe now' in email):
    spam = True
if('click this' in email):
    spam = True
print("spam is:", spam)
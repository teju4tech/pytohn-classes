'''program to input name,marks and phon.no of a student and format
   it using format function?
'''
'''MI Solution'''
Name = input("Enter Your Name: ")
Marks = input("Enter your marks: ")
phone = int(input("Enter your mo.no: "))

info = "The name of student {}\nThe marks is: {}.\nThe phon number:  {}".format(Name,Marks,phone)
print(info)

'''Mentor's Solution'''
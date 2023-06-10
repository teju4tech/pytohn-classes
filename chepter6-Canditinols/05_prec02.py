# Q-Write a program to find out whether a student is pass 
# or fail,if it requires total 40% and at least 33% in each
# subject to pass Asume 3 subject and take marks of input from the user ?

# User input
Maths = int(input("Maths marks:"))
Physics = int(input("Physics marks:"))
chem = int(input("chem marks:"))
English = int(input("English marks:"))
Sanskrit = int(input("Sanskrit marks:"))
# Totaling
Totalmarks = (Maths+Physics+chem+English+Sanskrit)
persentage = (Totalmarks/5)
# displays
print("Total marks:",Totalmarks)
print("Total persentage:",persentage)
# conditions
if(persentage>=40):
    if(Maths>=33 and Physics>=33 and chem>=33 and English>=33 and Sanskrit>=33):
        print("You'r pass")
else:
    print("you'r not pass")
# elif(Maths==33 && Physics==33 && chem=33 && English==33 && Sanskrit==33):
#     print("You'r pass")
# else:
#     print("You'r fail")


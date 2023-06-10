# Q-find a greade in students marks
M = int(input("Enter the marks of M:"))
M2 = int(input("Enter the marks of M:"))
M3 = int(input("Enter the marks of M:"))
M4 = int(input("Enter the marks of M:"))
M5 = int(input("Enter the marks of M:"))

totalMarks= (M+M2+M3+M4+M5)
persentage= (totalMarks/5)
if(persentage>=95):
    print("You'r greade is A+ ")
elif(persentage>=90):
    print("You'r greade is A ")
elif(persentage>=85):
    print("You'r greade is B+")
elif(persentage>=80):
    print("You'r greade is B")
elif(persentage>=75):
    print("You'r greade is C")
elif(persentage>=60):
    print("You'r greade is D")
elif(persentage>=33):
    print("You'r grade is E")
else:
    print("you'r grade is F")
    
print(persentage)
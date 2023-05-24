# Q-accept marks of 6 sub students and display them in a sorted manner ?
print("Enter your six subjects marks: ")
Maths = int(input("Enter the maths marks: "))
Physics = int(input("Enter the Physics marks: "))
Chemestry = int(input("Enter the Chemestry marks: "))
Sanskrit = int(input("Enter the Sanskrit marks: "))
Hindi = int(input("Enter the Hindi marks: "))

TotalMarks = [Hindi,Physics,Chemestry,Sanskrit,Maths]
TOtalmarks = ((Hindi+Chemestry+Maths+Sanskrit+Physics)/5)
TotalMarks.sort()
print(TotalMarks)
print(TOtalmarks)
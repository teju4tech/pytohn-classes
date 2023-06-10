# Q-ato find greatest of four numbers entered by the user ?
N1 =int(input("Enter the fisrt no: "))
N2 =int(input("Enter the sec. no: "))
N3 =int(input("Enter the three no: "))
N4 =int(input("Enter the four no: "))

if(N1>N2):
    Muxnum1 = N1
else:
    Muxnum1 = N2
if(N3>N4):
    Muxnum2 = N3
else:
    Muxnum2 = N4

if(Muxnum1>Muxnum2):
    print("Greatest number is: ",Muxnum1)
else:
    print("Greatest number is: ",Muxnum2)

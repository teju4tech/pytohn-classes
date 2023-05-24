# Q-check whether is number prime or something or not
#prime = it dived by itself or 1 only
num = int(input("Enter the num:"))
for i in range(2,num):
    if(num%i==0):
        print("Not prime")
        break
else:
    print("This is prime")    

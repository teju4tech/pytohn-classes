# Q-to print multiplication table of a given number sing for loop?
# M i approch
N = int(input("Enter the number:"))
for i in range(0,10):
    i += 1
    A =(N*i)
    print(A)
# Mentor approch
num = 10
for i in range(10):
    print(f"{num}x{i+1}={num*(i+1)}")


'''Store a mul table in a file.txt'''
'''Mi Solution'''
try:
    num = int(input("Enter a num: "))
    multi = [num*i for i in range(1,11)]
    # i = 1
    # for i in range(1,11):
    #     multi = i*num
    print(multi)
    with open("1.txt","w") as f:
        f.write(str(multi))
except Exception as e:
    print("The Error is:{e}")
else:
    print("Program is successful!!!")
finally:
    f.close()

'''Mentor's Solution'''

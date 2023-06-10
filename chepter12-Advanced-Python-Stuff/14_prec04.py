''' A progrm to display a/b where a and b are integers 
    if b=0 ,dispaly infinite by handling the ZeroDivision 
    Error ?
'''
try:
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    print(num1 / num2)

except ValueError:
    print("Int ki jgeh Int'j dalne ka kya")
except ZeroDivisionError:
    print("Ananta (infinity)")
except Exception as e:
    print(f"Error is: {e}!!!")
else:
    print("Try is successful!!")
finally:
    print("(Server1.0).close()")

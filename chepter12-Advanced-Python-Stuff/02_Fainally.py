'''[Fainally] - This keyword is using in try ecept and 
   fainally .This was always runing.
'''
try:
    A = int(input("Enter the a: "))
    B = int(input("Enter the B: "))
    print(A + B)
    print(A / B)
    if B>199:
        raise Exception("This is So badha")

except ValueError:
    print("This is value Error!!!")
except TypeError:
    print("This is type Error!!!")
except ZeroDivisionError:
    print("This is Zero division Error!!!")
except Exception as e:
    print(f"Error is:{e}")
else:
    print("Try is successful !!!")
finally:
    print("I AM finally !!")

print("Dekh Error k baad bhi print ho gya Na")

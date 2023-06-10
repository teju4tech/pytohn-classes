'''[EXCHEPTION HANDLING ]- When we wrote a program that is
   chance to crash or mal-function our program by our
   side our may be that we use any api or any server
   that server or api is not capable to run our program
   SO avoid this type situation we need to HANDLE our
   program by Own.
   [yE eNGLISH mENE likhi hai]
'''
'''if an error ocure in 10 lines therefore [fir bhi]
   the code after error will be runing.
'''
'''We can create our own Error Exception using
   raise keyword.
'''
'''The Else will be Runing only if try
   is successful
'''
try:
   print("This is addition")
   a = int(input("Enter the a: "))
   b = int(input("Enter the b: "))
   print(a + b)
   #giving inp 0
   print(a / b)
   if b>199:
      raise Exception("This is So Large")

except ValueError:
   print("There are value Error")

except ZeroDivisionError:
   print("This is Zero Division Error")

except  Exception as  e:
   print(f"The Error was: {e}")

else:
   print("Try is successful")

print("Dekh ho gya print Error k baad bhi")
'''a progm to open three files 1.txt,2.txt and 3.txt If 
   any of these files are not present , a message without
   exiting the prgrm must be printed prompting the same.
'''
'''MI code Solution'''
try:
   with open("1.txt","r") as f:
      text = f.read()

   with open("2.txt","r") as f:
      text1 = f.read()

   with open("3.txt","r") as f:
      text2 = f.read()

except FileNotFoundError:
   print("This  File is NotFound Error!!")   

except  Exception as e:
   print(f"The Error is: {e}")

else:
   print("Try is successful !!!")

finally:
   f.close()

'''Mentor's Solution'''
try:
   with open("1.txt","r") as f:
      text = f.read()
   with open("1.txt","r") as f:
      text = f.read()
   with open("1.txt","r") as f:
      text = f.read()

except Exception as e:
   print(f"Error Reason: {e}")
print("Thanks for using this program")



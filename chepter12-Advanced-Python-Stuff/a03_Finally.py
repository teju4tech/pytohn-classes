'''Many persons says that what the use of
   finally keyword.The use if we work on a 
   real world project we are need to close 
   files or servers and api's so if we don't
   use the finally keyword this will be harm
   for our project.
'''
'''Dhan se suno IS file ka naam hai a03_Finally.py
   dusri ka naam hai 04_main_name.py
   jab mene dusri me a03 ko import kiya
   or run kiya to ek folder bana
   _pycache__
   fir mene a03 k code se main_name ko # kark
   fun() or print ko ek kadam piche liya
   save kiya or fir 
   04 ko vaps run kiya 
   to a03 wala program waha 04 me 
   excute ho raha tha!!!
   or jab mene name ko print kara
   is file me yaha name hi print hua
   Lkin jab mene 04 file ko run kiya 
   to Literly module ka naam print
   hua ..
'''
def function():
     try:
         a = int(input("a:"))
         b = int(input("b:"))
         return a/b 
     except Exception as e:
        print(f"Error is: {e}")
        return 0
     finally:
         print("close the files.")
         print("if work is done or not")
    #  print("I will be always print")


print(__name__)
if __name__ == '__main__':
   function()
   print("main")
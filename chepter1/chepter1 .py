import pyttsx3 #this is moduel
import os #this is moduel
engine = pyttsx3.init()
#speak-function
engine.say("Can you see the content of This Directry..")
engine.say("Press Y")
engine.runAndWait()
#work-function
A = int(input("ENter: "))
if(A == 1):
    engine.say("Dekh bhai")
    print(os.listdir())
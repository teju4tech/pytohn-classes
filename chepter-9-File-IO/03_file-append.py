'''Append mode adding more line to the programmm'''


f = open("write.py",'a')
f.write("print('Hello')")
f.write("\nd=0\n")
f.write("while(d!=1):\n")
f.write("\t\tprint('raju')\n")
f.write("\t\td += 1")
f.close()
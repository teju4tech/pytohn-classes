'''Write mode rewrite the programm again and again'''
f = open("write.py",'w')
f.write("print('Hello')")
f.write("\nfor i in range(2,9):\n")
f.write("print(i)")
f.close()

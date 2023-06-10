'''Q- Repeat pr-4 for a list of sach words to be considerd ?
'''
with open("data.py","r") as f:
    text = f.read()

text = text.replace('ironman','Bhahubali')

with open("data.py","w") as f:
    text = f.write(text)


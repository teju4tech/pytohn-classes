# Q- Ditect double spaces in a string ?
myStr = "Yo bro  bhai  tu bade  dino  baad dikh raha h"
khali = (myStr.find("  "))
print(khali,"h be ")
if(khali>1):
    print("Do se jyada h")
else:
    print("Ek bhi na dikhi")

nwmyStr=(myStr.replace("  "," "))
print(nwmyStr)
print(myStr)

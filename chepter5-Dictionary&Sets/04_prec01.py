# Q-Creat dic of hindi words with his value as their English translation ?
Mydic = {
    "Bhai": "Brother",
    "Batal": "Bottle",
    "sher": "Lion",
    "Goat": "Legend",
    "Ghadhi": "Watch"
}

key= input("Enter a key: ")
if(Mydic.get(key)==None):
    print("Hey!!\n This will not in a dict.")
else:
    print("The value of key is: ",Mydic.get(key))
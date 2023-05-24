oxford = {
 "Gift":"Something special for someone special"
 ,"Bottle": "To store water or some liqueid",
 "This": "A keyword in C++",
 "Youtube":"A video sharing platform",
 "instagram":"A picture sharing platform",
 "Mylist": [12,34,21,45]
}

# Methods
# It's shows tuple of items
print(oxford.items())
# same method but menually
print("\n\n---|Menally|---")
for a, b in oxford.items():
    print(a,"=",b)

print("\nAnother method")
for key in oxford.keys():
    print(key)

print("\n")
oxford.update({"Teju":"Uchiha","Naziz":"uzimaki"})
for a,b in oxford.items():
    print(a,"=",b)

# print(oxford['notpresent'])
print(oxford.get('notpresent'))



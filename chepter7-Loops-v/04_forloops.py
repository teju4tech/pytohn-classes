# Interview Quetions?
# Can we use for loop with else ?
a = [1,2,3,4,5]
for item in a:
    print(item)
    if(item==4):
        continue
    print("done",item)
else:
    print("We are inside else")
    #for the excution of else is needed to done all the itretions
    # break-break the loop for a condition
    #continue-it will continue the loop escap the candition
print("we have finished this loop")
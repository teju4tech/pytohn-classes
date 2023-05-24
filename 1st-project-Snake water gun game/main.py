'''Rule of game 
               1)There is three sub snake,water and Gun
               2)if snake vs water sanke will drink snake win
               3)if snake vs gun gun shoot the snake gun win
               4)if gun vs  water water win
'''

import random

''' Creating a function '''
def swg(comp, mine):
    if(comp==mine):
        return None
    if(comp=='s' and mine =='g'):
        return True
    elif(comp=='w' and mine=='s'):
        return True
    elif(comp=='g' and mine=='w'):
        return True
    else:
        return False
    
choice = ('s','w','g')
comp = random.randint(0,2)
comp = choice[comp]
mine = input('choos snake for s,water for w,gun for g: ')

win = swg(comp, mine)
if win:
    print(f"U chose {mine} and the computer chose {comp}")
    print("You won")
elif win is None:
    print("Match Drawn")
else:
    print(f"You chose {mine} and the computer chose {comp}")
    print("You loose")
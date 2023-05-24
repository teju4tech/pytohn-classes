''' Made a game who Guess the perfact number'''
import random
 
A = 0
G = random.randint(1,100)
print("\n\n-----|Only 5 chance to win this game|-----\n\n")
while(A!=10):
    A += 1
    '''computer vs computer'''
    # N = random.randint(1,100)
    ''' player vs computer'''
    N = int(input("Enter the Guess: "))
    print(G)
    if(G>N):
        print(f"{N} is less for Your Guess!!")
        print(f"{A} chance is done")
    elif(G<N):
        print(f"{N} is greator then Guess!!")
        print(f"{A} chance is done")
    elif(G==N):
        print(f"{N} is Parfact You won!!")
        print(f"{A} chance is done")
    else:
        None



import random
x=random.randint(1,99)

try_again ="yes"
        
while try_again=="yes" or try_again =="y":
        
    y=int(input("ENTER A NUMBER BETWEEB 1 AND 99: "))

    if(y==x):
         print('CORRECT GUESS')
    elif(y<x):
        print('GUESSED TOO LOW')

    else:
         print('TOO HIGH')

    print("ACTUAL OUTPUT",x)
        
    try_again = input("try again??")
        
    

import random


try_again ="yes"
score=0
        
while try_again=="yes" or try_again =="y":
    x=random.randint(1,99)
    y=int(input("ENTER A NUMBER BETWEEB 1 AND 99: "))

    if(y==x):
         print('CORRECT GUESS')
         score=score+1
    elif(y<x):
        print('GUESSED TOO LOW')

    else:
         print('TOO HIGH')
    print("ACTUAL OUTPUT",x)
    print("TOTAL SCORE: ",score)
         
    
   
        
    try_again = input("PRESS y OR yes to try again??\n PRESS any key to exit: ")
   
        
   

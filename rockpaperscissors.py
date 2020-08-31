import random

score = 0
try_again ="yes"
t =["rock","paper","scissor"]
        
while try_again=="yes" or try_again =="y":
    cpu=random.choice(t)
    print("CHOICES:\n rock \n paper \n scissor")
    player=(input("ENTER YOUR CHOICE: "))
    print("CPU CHOICE:",cpu)
    print("YOUR CHOICE:",player)
    print("RESULT:")
    if(cpu == player):
         print('TIE!!')
         
    elif(cpu=="rock"):
        if(player=="scissor"):
            print("you lost")
        else:
            print("you won!!")
            score+=1

    elif(cpu=="paper"):
        if(player=="rock"):
            print("you lost")
        else:
            print("you won!!")
            score+=1
            
    elif(cpu=="scissor"):
        if(player=="paper"):
            print("you lost")
        else:
            print("you won!!")
            score+=1
    
        
    try_again = input("PRESS y OR yes to try again??\n PRESS any key to exit: ")
    print("total score:",score)
   
        
   

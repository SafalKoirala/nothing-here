import pygame
pygame.init()

win = pygame.display.set_mode((500,500)) #window size
pygame.display.set_caption("First Game") #window title

x = 10 #initial postion of rectangle x,y
y = 10
width = 40  #size of rectangle
height = 40
vel =   20  #speed of movement
isJump = False
jumpcount =10

run = True

while run:
    pygame.time.delay(100) #delay in milisec

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() #movement define gareko ani paxadi ko part boundary ma rakhna lai
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel :
        x += vel
     if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_space]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -=(jumpcount **2)*0.5
            jumpCount -=1
        else:
             
    win.fill((0,0,0))  # Fills the screen with black so that it looks like moving
    pygame.draw.rect(win, (250,20,20), (x, y, width, height))   #rectangle ko color ra postion and size
    pygame.display.update() #to show change in postion
    
pygame.quit() #mathi ko cross lain functionig garauna

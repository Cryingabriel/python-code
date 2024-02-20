import pygame
import random
import math
import winsound
from pygame.math import Vector2

pygame.init()
pygame.display.set_caption("Simon!")
screen = pygame.display.set_mode((800,800))




def collision(xpos,ypos):
    if math.sqrt((xpos - 400)**2 + (ypos - 400)**2) > 200 or math.sqrt((xpos - 400)**2 + (ypos - 400)**2)< 100:
        print ("outside of the ring")
        return -1
    elif xpos < 400 and ypos < 400:
        print("over the red button")
        return 0
    elif xpos < 400 and ypos > 400:
        print("over the green button")
        return 1
    elif xpos > 400 and ypos > 400:
        print("over the blue button")
        return 2
    elif xpos > 400 and ypos > 400:
        print("over the yellow button")
        return 3
#variables
xpos = 0
ypos = 0
Mousepos = (xpos,ypos)
hasclicked = False
pattern = []
playerpattern = []
playerTurn = True
pi = 3.14159
ded = False


    




while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        break
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        hasclicked = True
        print("clicked")
    if event.type == pygame.MOUSEBUTTONUP:
        hasclicked = False
    
    if event.type == pygame.MOUSEMOTION:
        Mousepos = event.pos
    
    #update section
    pattern.append(random.randrange(0,4))

    for i in range(len(pattern)):
        if pattern[i] == 0: #RED
            pygame.draw.arc(screen, (255,0,0), (200,200,400,400), (2*pi), (pi/2), 100)
            pygame.display.flip()
            winsound.Beep(440, 200)
        elif pattern[i] == 1: #GREEN
            pygame.draw.arc(screen, (0,255,0), (200,200,400,400), pi/2, pi, 100)
            pygame.display.flip()
            winsound.Beep(540, 300)
        elif pattern[i] == 2: #BLUE
            pygame.draw.arc(screen, (0,0,255), (200,200,400,400), (3 * pi / 2), (2*pi), 100)
            pygame.display.flip()
            winsound.Beep(640, 400)
        elif pattern[i] == 3:
            pygame.draw.arc(screen, (255,255,0), (200,200,400,400), pi,(3 * pi / 2), 100)
            pygame.display.flip()
            winsound.Beep(740, 500)

    #render section
    collision(Mousepos[0], Mousepos[1])
    pygame.draw.arc(screen, (0,155,0), (200,200,400,400), pi/2, pi, 100)
    pygame.draw.arc(screen, (155,155,0), (200,200,400,400), pi,(3 * pi / 2), 100)
    pygame.draw.arc(screen, (0,0,155), (200,200,400,400), (3 * pi / 2), (2*pi), 100)
    pygame.draw.arc(screen, (155,0,0), (200,200,400,400), (2*pi), (pi/2), 100)
    pygame.time.wait(800)
    pygame.display.flip()

pygame.quit()
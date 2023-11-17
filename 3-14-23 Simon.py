import pygame
import random
import math
import winsound

pygame.init()
pygame.display.set_caption("Simon")
screen = pygame.display.set_mode((800,800))


def collision(xpos, ypos):
   # print("inside collision function")
    if math.sqrt((xpos - 400) ** 2 + (ypos - 400) ** 2)> 200 or math.sqrt((xpos - 400) ** 2 + (ypos - 400) ** 2)< 100:
        print("outside of ring")
        return -1
    elif xpos < 400 and ypos < 400:
        print("over the Red button")
        pygame.display.flip()
        winsound.Beep(440,500)
        return 0
    elif xpos < 400 and ypos > 400:
        print("Over the Green button")
        return 1
    elif xpos > 400 and ypos < 400:
        print("Over the Blue button")
        return 2
    elif xpos > 400 and ypos > 400:
        print("Over the Yellow button")
        return 3

#variables
moupos = (0, 0)
hclicked = False
pattern = []
ppattern = []
pturn = False
pi = 3.14159
ded = False

#Draw everything first so things don't appear one at a time
pygame.draw.arc(screen, (155, 0, 0), (200, 200, 400, 400), pi/ 2, pi, 100)
pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (2 * pi), (pi / 2), 100)
pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3 * pi / 2), (2 * pi), 100)
pygame.display.flip()


while True:
    collision(moupos[0],moupos[1])
    event = pygame.event.wait()#event queue
    
    #input section
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.MOUSEBUTTONDOWN:
        hclicked = True
        print("click")
    
    if event.type == pygame.MOUSEBUTTONUP:
        hclicked = False

    if event.type == pygame.MOUSEMOTION:
        moupos = pygame.mouse.get_pos()
    # update section---------------------
    print("starting player turn")
    if pturn == True:
        if len(ppattern) < len(pattern):
            if hclicked== True:
                ppattern.append(collision(moupos[0], moupos[1]))
                hclicked= False
    else:
        pturn = False
        #pygame
    #play computer screen 
    if pturn == False:
        print("Starting machine Turn")
        pattern.append(random.randrange(0, 3))
        for i in range(len(pattern)):
            if pattern[i] == 0:
                pygame.draw.arc(screen, (255, 0, 0), (200, 200, 400, 400), pi/ 2, pi, 100)
                pygame.display.flip()
                pygame.time.wait(800)
            elif pattern[i] == 2:
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), (2 * pi), (pi / 2), 100)
                pygame.display.flip()
                winsound.Beep(840, 500)

            elif pattern[i] == 3:
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), (3 * pi / 2), (2 * pi), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)
        ppattern.append(collision(moupos[0],moupos[1]))
        print(ppattern)
        pygame.draw.arc(screen, (155, 0, 0), (200, 200, 400, 400), pi/ 2, pi, 100)
        pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
        pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (2 * pi), (pi / 2), 100)
        pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3 * pi / 2), (2 * pi), 100)
        pygame.display.flip()
        #pygame.time.wait(800)
        pturn = True
        ppattern.clear()
    #render section---------------------
    
    #game board
    pygame.draw.arc(screen, (155, 0, 0), (200, 200, 400, 400), pi/ 2, pi, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (2 * pi), (pi / 2), 100)
    pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3 * pi / 2), (2 * pi), 100)
    pygame.display.flip()
pygame.quit()

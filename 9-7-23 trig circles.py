import pygame
import math
pygame.init()
pygame.display.set_caption("Graphical for loops")
screen = pygame.display.set_mode((800, 800))

gameover = False
angle = 0

while gameover == False:

    angle += 1
    if angle > 360:
        angle = 0
    
    radians = angle/180*3.14

    xpos = 400*math.cos(radians) + 400
    ypos = 400*math.sin(radians) + 400

    pygame.draw.circle(screen, (250, 250, 0), (xpos, ypos), 2)

    pygame.display.flip()

pygame.quit()
import random
from random import randrange as rr
import pygame
import math

screen = pygame.display.set_mode((800, 800))

def drawsnow( lev, x1, y1, x5, y5):
    if lev == 0:
        if lev < 10:
            pygame.draw.line(screen, (rr(5,200), rr(5,200), rr(5,200)), (x1, y1), (x5, y5))
        else:
            pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x5, y5), 1)
        
        pygame.display.flip()

    else:
        deltaX = x5 - x1
        deltaY = y5 - y1

        x2 = x1 + deltaX / 3
        y2 = y1 + deltaY /3

        x4 = x1 + deltaX * 2/3
        y4 = y1 + deltaY * 2/3

        x3 = ((x2 + x4) + math.sqrt(3) * (y2 - y4))/2
        y3 = ((y2 + y4) + math.sqrt(3) * (x4 - x2))/2

        drawsnow(lev-1, x1, y1, x2, y2)
        drawsnow(lev-1, x2, y2, x3, y3)
        drawsnow(lev-1, x3, y3, x4, y4)
        drawsnow(lev-1, x4, y4, x5, y5)


level = 0
while True:
    level += 1
    drawsnow(level, 500, 500, 600, 400)
    drawsnow(level, 400, 400, 500, 500)
    drawsnow(level, 400, 300, 600, 500)
    pygame.display.flip()
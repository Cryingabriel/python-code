import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set the window title
pygame.display.set_caption("Pythagorean Tree Fractal")

# Create the game screen
screen = pygame.display.set_mode((1500, 900))
r = True

def tree(ax, ay, bx, by, depth=0):


    if depth > 0:

        # (ax, ay) is bottom left corner
        # (bx, by) is bottom right corner

        # find the length of a side
        dx = bx - ax
        dy = ay - by

        # find top ight corner
        x3 = bx - dy
        y3 = by - dx

        #find top eft corner
        x4 = ax - dy
        y4 = ay - dx

        # find midpoint
        x5 = x4 + (dx - dy) / 2
        y5 = y4 - (dx + dy) / 2

        #top left to bottom left
        pygame.draw.line(screen, (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255)), (x4, y4), (ax, ay))#WHITE

        # Line from bottom left to bottom right
        pygame.draw.line(screen, (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255)), (ax , ay ), (bx , by )) #RED
            
        # line from bottom right corner to top right corner
        pygame.draw.line(screen, (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255)), (bx , by ), (x3 , y3 ))#GREEN  
        #top left to top right
        pygame.draw.line(screen, (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255)), (x3, y3), (x4, y4))#BLUE
            
        

        if depth > 10:
            pygame.display.flip()

        # Recursively call the tree function for the two smaller branches
        tree(x4, y4, x5, y5, depth - 1)  # Left branch
        tree(x5, y5, x3, y3, depth - 1)  # Right branch

# Initial call to the tree function to start the fractal
while r == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close game window
            break
    color = (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))
    tree(600, 850, 800, 850, depth=20)
    screen.fill(color)
    pygame.display.flip()
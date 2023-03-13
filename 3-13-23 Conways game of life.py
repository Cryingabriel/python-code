import pygame
import random

pygame.init()
pygame.display.set_caption("Game of life")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

map = [[random.random() > .7 for i in range(16)] for i in range (16)]



while True:
    clock.tick(60) #FPS
    event = pygame.event.get() #event queue
    map1 = map.copy()
    #input section___________
    for event in pygame.event.get():
        break
    #update section --------------
    for i in range(16):
            for j in range(16):
                
                if map[i][j]==0:
                    pygame.draw.rect(screen, (0, 0, 0), (j*50, i*50, 50, 50)) #this is making the squares black if it's not 1
                    pygame.draw.rect(screen, (255, 255, 255), (j*50, i*50, 50, 50), 1) #this shows the grid
                if map[i][j]==1:
                    r = random.randrange(0,255)
                    g = random.randrange(0,255)
                    b = random.randrange(0,255)
                    pygame.draw.rect(screen, (r, g, b), (j*50, i*50, 50, 50)) #this is making the squares light blue if it's not 0
                counter = 0#reset the counter for each cell
                if i < 15 and map[i+1][j] == 1: #checks above
                    counter += 1
                if i >= 0 and map[i-1][j] == 1: #checks below
                    counter += 1
                if j < 15 and map[i][j+1] == 1: #checks right
                    counter += 1
                if j >= 0 and map[i][j-1] == 1: #checks left
                    counter += 1
                if i < 15 and j < 15 and map[i+1][j+1] == 1: #checks top right corner
                    counter += 1
                if i >= 0 and j >= 0 and map[i-1][j-1] == 1: #checks the bottom left corner
                    counter += 1
                if i < 15 and j >= 0 and map[i+1][j-1] == 1: #checks top left corner
                    counter += 1
                if j < 15 and i >= 0 and map[i-1][j+1] == 1: #checks bottom right corner
                    counter += 1
                if map[i][j] == 1 and counter <=1:
                    map1[i][j] = 0
                    print("I died from lonliness")
                if map[i][j] == 1 and counter >=4:
                    map1[i][j] = 0
                    print("I have died")
                if map[i][j] == 0 and counter == 3:
                    map1[i][j] = 1
                    print("I have been born")
    pygame.time.wait(60)
    map = map1
    #render section-------------------
 
    
    #stuff gets drawn here!

    pygame.display.flip()
 #end game loop------------------------------


pygame.quit()
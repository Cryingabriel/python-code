import pygame
from pygame.math import Vector2
import random
from random import randint as rr
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))

mexit = False

class Box():
    def __init__(self, xpos, ypos, mass):
        self.pos = Vector2(xpos, ypos)
        self.xv = 10
        self.yv = 0
        self.num = random.randint(0,2)
        self.gavity = False
        self.c = 0
        self.mass = mass
        self.v2 = 0
    
    def draw(self):
        pygame.draw.rect(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x, self.pos.y, 20, 20))
    
    def move(self):
        if self.pos.x >= 780 or self.pos.x <= 0:
            self.xv *= -1
            self.c +=1
        if self.pos.y >=780:
                self.gavity = True

        if self.gavity == False:
            self.yv = 10
        elif self.gavity == True:
            self.yv = 0


        self.pos.x += self.xv
        self.pos.y += self.yv

    def collision(self,b2x, b2m):
        if self.pos.x <= b2x and self.pos.x >= b2x:
            self.xv *= -1
            self.c +=1
            self.v2 = (self.mass - b2m)/ (self.mass + b2m)
            self.xv = self.v2
        print("box 1 c at", self.c)
        


class Box2():
    def __init__(self, xpos, ypos, mass):
        self.pos = Vector2(xpos, ypos)
        self.xv = -10
        self.yv = 0
        self.num = random.randint(0,2)
        self.gavity = False
        self.c = 0
        self.mass = mass
        self.v2 = 0
    def draw(self):
        pygame.draw.rect(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x, self.pos.y, 80, 80))

    def move(self):
        if self.pos.x >= 720 or self.pos.x <= 0:
            self.xv *= -1
            self.c +=1
        if self.pos.y >=720:
            self.gavity = True

        if self.gavity == False:
            self.yv = 10
        elif self.gavity == True:
            self.yv = 0


        self.pos.x += self.xv
        self.pos.y += self.yv

    def collision(self,b1x, b1m):
        if self.pos.x <= b1x and self.pos.x >= b1x:
            self.xv *= -1
            self.c +=1
            self.v2 = (b1m*2)/ (b1m + self.mass)
            self.xv = self.v2
        print("box 2 c at", self.c)
        
        #if self.pos.x >=


b1 = Box(200, 780, 1)

b2 = Box2(600, 720, 100)

while not mexit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mexit = True





    screen.fill((0,0,0))

    b1.collision(b2.pos.x, b2.mass)
    b2.collision(b1.pos.x, b1.mass)

    b1.move()
    b2.move()

    

    b1.draw()
    b2.draw()
    pygame.display.flip()


pygame.quit()
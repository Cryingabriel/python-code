import pygame
from random import randrange as rr
from pygame.math import Vector2
import math
pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
fr = int(input("How many turkeys would you like to appear?"))
turkeys = fr
screen = pygame.display.set_mode((800, 800))
exit = False
clock = pygame.time.Clock()
ran = rr(0,800)
xpos = 0
ypos = 0
score = 0
mousepos = (xpos,ypos)

class Clouds():
    def __init__(self, xpos, ypos):#setting up all of the class specific variables
        self.pos = Vector2(xpos, ypos)
        self.vx = -5
        self.radius = 10
    
    def draw(self):
        #Drawing my clouds in the background
        pygame.draw.circle(screen, (255,255,255), (self.pos.x, self.pos.y), 10)
        pygame.draw.circle(screen, (255,255,255), (self.pos.x + 10, self.pos.y), 10)
        pygame.draw.circle(screen, (255,255,255), (self.pos.x + 20, self.pos.y), 10)

    def move(self):
        if self.pos.x < 0:#once the cloud moves out of screen it appears to the right and scrolls back on screen
            self.pos.x = 850
        self.pos.x += self.vx
r = []
for i in range(10):
    r.append(Clouds(rr(0,800), rr(0,400)))

class Turkey():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.vy = 5
        self.vy2 = 10
        self.xv = rr(10,20)
        self.alive = True
        self.radius1 = 30
        self.radius2 = 60
        self.clicked1 = False
        self.score = 0
        self.size1 = 10
        self.num = rr(0,2)

    def draw(self):#draw the turkey
        if self.alive == True:
            #Feathers
            #The overall shape of the turkey is from my teacher Dr.Mo however the size, placement and color is all me.
            pygame.draw.circle(screen, (255,174,66), (self.pos.x+5, self.pos.y), self.size1)
            pygame.draw.circle(screen, (255,174,66), (self.pos.x+15, self.pos.y-22), self.size1)
            pygame.draw.circle(screen, (255,174,66), (self.pos.x+35, self.pos.y-35), self.size1)
            pygame.draw.circle(screen, (255,174,66), (self.pos.x+55, self.pos.y-22), self.size1)
            pygame.draw.circle(screen, (255,174,66), (self.pos.x+65, self.pos.y), self.size1)
            pygame.draw.circle(screen, (255,213,0), (self.pos.x+9, self.pos.y-11), self.size1)
            pygame.draw.circle(screen, (255,213,0), (self.pos.x+25, self.pos.y-30), self.size1)
            pygame.draw.circle(screen, (255,174,66), (self.pos.x+45, self.pos.y-30), self.size1)
            pygame.draw.circle(screen, (255,213,0), (self.pos.x+45, self.pos.y-30), self.size1)
            pygame.draw.circle(screen, (255,213,0), (self.pos.x+60, self.pos.y-11), self.size1)
            #Legs
            pygame.draw.rect(screen, (150,75,0), (self.pos.x+20, self.pos.y+10, 10, 30))
            pygame.draw.rect(screen, (150,75,0), (self.pos.x+40, self.pos.y+10, 10, 30))
            #Body
            pygame.draw.circle(screen, (150,75,0), (self.pos.x+35, self.pos.y), 30)
            pygame.draw.ellipse(screen, (150,75,0), (self.pos.x+23, self.pos.y-40, 25, 40))
            #Face
            pygame.draw.polygon(screen, (255,200,100), ((self.pos.x+30, self.pos.y-30), (self.pos.x+35, self.pos.y-15), (self.pos.x+41, self.pos.y-30)))
            pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+28, self.pos.y-30), 5)
            pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+28, self.pos.y-30), 3)
            pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+43, self.pos.y-30), 5)
            pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+43, self.pos.y-30), 3)
    def addscore(self):
        return self.score
    def S(self):
        self.score = 0

    def move(self):
        if self.alive == True:
            if self.num == 0:
                self.vy
                self.pos.y += self.vy #
            elif self.num == 1:
                self.vy2
                self.pos.y += self.vy2
            if self.pos.y >= 800:#if the y position of the turkey is below 800 set turkey to -100 y position
                self.pos.y = -100
            self.pos.x += self.xv

            if self.pos.x >=800:#make the turkeys bounce back and forth
                self.xv *= -1
            elif self.pos.x <=0:
                self.xv *= -1

    def collision(self):
        if self.alive == True:
            #My teacher Dr.Mo provided the distance formula
            if math.sqrt((mousepos[0]-self.pos.x-35)**2 + (mousepos[1]-self.pos.y)**2)<self.radius1: #if the mouse is within the turkeys body, kill it
                print("ah")
                self.score += 1
                self.clicked1 = True
                if self.clicked1 == True:
                    self.alive = False
                else:
                    self.clicked1 = False

        return self.alive   
l = []
for i in range(fr):#how many turkeys are made
    l.append(Turkey(rr(0,800), rr(0,800))) #put all of the turkeys into a list

while exit == False:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(l)):
                l[i].collision()

        if event.type == pygame.MOUSEMOTION: #check if mouse moved
            mousepos = event.pos #refreshes mouse position

    #render section
    screen.fill((145,224,255))

    for i in range(len(r)):
        r[i].move()
        r[i].draw()

    for i in range(len(l)):
        l[i].move()
        l[i].draw()

        score += l[i].addscore()
        turkeys -= l[i].addscore()
    for i in range(len(l)):
        l[i].S()

    if turkeys == 0:#p
        text_label2 = my_font.render(str("YOU WIN! "),1,(0, 0, 0))
        screen.blit(text_label2, (325,380))

    text_label3 = my_font.render(str("Score: "),1,(0, 0, 0))
    text_surface = my_font.render(str(score), 1 ,(0, 0, 0))

    text_label1 = my_font.render(str("Turkeys Left: "),1,(0, 0, 0))
    text_surface1 = my_font.render(str(turkeys), 1 ,(0, 0, 0))

    screen.blit(text_surface1, (200,30))
    screen.blit(text_label1, (0,30))
    screen.blit(text_surface, (90,0))
    screen.blit(text_label3, (0,0))

    pygame.display.flip()
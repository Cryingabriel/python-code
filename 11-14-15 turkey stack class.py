import pygame
from random import randrange as rr
from pygame.math import Vector2
import math

pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((800, 800))
exit = False
clock = pygame.time.Clock()

xpos = 0
ypos = 0
score = 0
fr =100
turkeys = fr
mousepos = (xpos,ypos)
ong = rr(0, 255)

class Turkey():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.vy = 5
        self.vy2 = 10
        self.xv = rr(10,20)
        self.num = rr(0,2)
        self.alive = True
        self.radius1 = 30
        self.radius2 = 60
        self.clicked1 = False
        self.score = 0
    
    def draw(self):
        if self.alive == True:
            if self.num == 0:
                #Feathers
                pygame.draw.circle(screen, (ong,rr(0,255),rr(0,255)), (self.pos.x+5, self.pos.y), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+15, self.pos.y-22), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+35, self.pos.y-35), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+55, self.pos.y-22), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+65, self.pos.y), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+9, self.pos.y-11), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+25, self.pos.y-30), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+45, self.pos.y-30), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+45, self.pos.y-30), 10)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+60, self.pos.y-11), 10)

                #Legs
                pygame.draw.rect(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+20, self.pos.y+10, 10, 30))
                pygame.draw.rect(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+40, self.pos.y+10, 10, 30))

                #Body
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+35, self.pos.y), 30)
                pygame.draw.ellipse(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+23, self.pos.y-40, 25, 40))
                #Face
                pygame.draw.polygon(screen, (rr(0,255),rr(0,255),rr(0,255)), ((self.pos.x+30, self.pos.y-30), (self.pos.x+35, self.pos.y-15), (self.pos.x+41, self.pos.y-30)))
                pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+28, self.pos.y-30), 5)
                pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+28, self.pos.y-30), 3)
                pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+43, self.pos.y-30), 5)
                pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+43, self.pos.y-30), 3)
            elif self.num == 1:
                #Feathers
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+5, self.pos.y), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+30, self.pos.y-32), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+65, self.pos.y-55), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+100, self.pos.y-32), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+120, self.pos.y), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+15, self.pos.y-15), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+45, self.pos.y-45), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+90, self.pos.y-45), 20)
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+115, self.pos.y-12), 20)

                #Legs
                pygame.draw.rect(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+40, self.pos.y+10, 20, 60))
                pygame.draw.rect(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+70, self.pos.y+10, 20, 60))

                #Body
                pygame.draw.circle(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+65, self.pos.y), 50)
                pygame.draw.ellipse(screen, (rr(0,255),rr(0,255),rr(0,255)), (self.pos.x+45, self.pos.y-65, 40, 60))
                #Face
                pygame.draw.polygon(screen, (rr(0,255),rr(0,255),rr(0,255)), ((self.pos.x+55, self.pos.y-45), (self.pos.x+65, self.pos.y-15), (self.pos.x+75, self.pos.y-45)))
                pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+50, self.pos.y-45), 10)
                pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+50, self.pos.y-45), 5)
                pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+80, self.pos.y-45), 10)
                pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+80, self.pos.y-45), 5)
    def addscore(self):
        return self.score
    def S(self):
        self.score = 0

    def move(self):
        if self.alive == True:
            if self.num == 0:
                self.pos.y += self.vy
            else:
                self.pos.y += self.vy2
            if self.pos.y >= 800:
                self.pos.y = -100
            self.pos.x += self.xv

            if self.pos.x >=800:
                self.xv *= -1
            elif self.pos.x <=0:
                self.xv *= -1

    def collision(self):
        if self.alive == True:
            if self.num == 0:
                if math.sqrt((mousepos[0]-self.pos.x-35)**2 + (mousepos[1]-self.pos.y)**2)<self.radius1:
                    print("ah")
                    self.score += 1
                    self.clicked1 = True
                    if self.clicked1 == True:
                        self.alive = False
                    else:
                        self.clicked1 = False
            elif self.num == 1:
                if math.sqrt((mousepos[0]-self.pos.x-60)**2 + (mousepos[1]-self.pos.y)**2)<self.radius2:
                    print("ah")
                    self.score += 1
                    self.clicked1 = True
                    if self.clicked1 == True:
                        self.alive = False
                    else:
                        self.clicked1 = False

        return self.alive
            


l = []
for i in range(fr):
    l.append(Turkey(rr(0,800), rr(0,800)))


while exit == False:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gover = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(l)):
                l[i].collision()

        if event.type == pygame.MOUSEMOTION: #check if mouse moved
            mousepos = event.pos #refreshes mouse position

    screen.fill((0,0,0))
    for i in range(len(l)):
        l[i].move()
        l[i].draw()

        score += l[i].addscore()
        turkeys -= l[i].addscore()
    for i in range(len(l)):
        l[i].S()

    if turkeys == 0:
        text_label2 = my_font.render(str("YOU WIN! "),1,(rr(0,255),rr(0,255),rr(0,255)))
        screen.blit(text_label2, (375,400))

    text_label3 = my_font.render(str("Score: "),1,(rr(0,255),rr(0,255),rr(0,255)))
    text_surface = my_font.render(str(score), 1 ,(rr(0,255), rr(0,255), rr(0,255)))

    text_label1 = my_font.render(str("Turkeys Left: "),1,(rr(0,255),rr(0,255),rr(0,255)))
    text_surface1 = my_font.render(str(turkeys), 1 ,(rr(0,255), rr(0,255), rr(0,255)))

    screen.blit(text_surface1, (200,30))
    screen.blit(text_label1, (0,30))
    screen.blit(text_surface, (90,0))
    screen.blit(text_label3, (0,0))

    pygame.display.flip()
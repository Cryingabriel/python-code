import pygame
import random
pygame.init()
pygame.display.set_caption("tap tap jump")
screen = pygame.display.set_mode((800,900))
clock = pygame.time.Clock()


gover = False

Mxpos = 0
Mypos = 0
mousePos = (Mxpos, Mypos)

#Player variables_______
scored = False
xpos = 200
ypos = 700
xVel = 1.5
yVel = 0
Might = False
Meft = False
mup = False
isOnGround = True
p1Score = 0
timervar = 300
font = pygame.font.SysFont('Comic Sans MS', 74)
font2 = pygame.font.SysFont('Comic Sans MS',40)
loserL = font2.render(str("YOU  LOSE + L  TAKEN"), 1, (255,0,0))
loserL2 = font2.render(str("+ YOUR'E   NOT  LE'BRON"), 1, (255,0,0))
class Basket():

    def __init__(self):
        self.xpos = 700
        self.ypos = 400
        self.alive = True
    def move(self):
        ranpos = random.randint(100,600)
        self.ypos = ranpos
    def getpos(self):
        return self.ypos
    def draw(self):
        pygame.draw.rect(screen, (241,241,241), (self.xpos, self.ypos, 70, 40))
        pygame.draw.rect(screen, (241,111,29), (self.xpos, self.ypos, 70, 10))
        pygame.draw.rect(screen, (241,111,29), (self.xpos+70, self.ypos-50, 10, 90))


basket = Basket()

while gover == False:
    timervar -=1 
    if timervar < 0:
        gover = True
    while gover == True:
        screen.blit(loserL,(100,400))
        screen.blit(loserL2,(100,480))
        pygame.display.flip()

    #game sh*t
    clock.tick(60)
    xpos+=xVel
    #keyt input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gover = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            yVel = -16
            xVel = 2.2

    #physiscikcx

    if ypos < 699:
        yVel +=.5
    elif ypos > 700:
        ypos = 700
        yVel = 0
        xVel = 1.5
    if xVel < 1.5:
        xVel += 0.1
    if xpos > 830:
        xpos = 200
    xpos += xVel
    ypos += yVel

   #SCORING
    if xpos >= 700 and xpos <= 770:
        if ypos >= basket.getpos() and ypos <= basket.getpos()+40:
            if yVel >= 1:
                if scored == False:
                    p1Score +=1
                    scored = True
                    basket.move()
                    timervar = 300
    if ypos > basket.getpos()+60:
        scored = False

    #rendering section
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    screen.fill((r,g,b))
    pygame.draw.circle(screen, (241,111,29), (xpos, ypos), 25)
    text = font.render(str(p1Score), 1, (255,255,0))
    timer = font.render(str(timervar), 1, (255,255,255))
    pygame.draw.line(screen, (40,255,0), (0,2),(timervar*2.6,2),10)
    basket.draw()
    screen.blit(text, (495,10))
    screen.blit(timer,(290,10))
    pygame.display.flip()
    print(yVel)
    







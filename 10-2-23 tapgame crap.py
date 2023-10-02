import pygame
from pygame.math import Vector2
import random
import math
pygame.init()
pygame.display.set_caption("Spin Hunter")
screen = pygame.display.set_mode ((800, 800))
Bye = False
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
coins = 0
playerPos = Vector2(380,390)
enemyPos = Vector2(random.randint(0,800),random.randint(0, 800))
clicked = False
playerDamage = 10
enemy = list()
xchoice = [0,800]

#TICKS
time = pygame.time.Clock()
ticks = 0
#PLAYER --------------------------------------------------------------------------------
class Player:
    def __init__(self,xpos,ypos, damage):
        self.pos = Vector2(xpos,ypos)
        self.damage = damage

    def draw(self):
        pygame.draw.rect(screen, (255,255,255), (self.pos, (20, 40)))

player = Player(playerPos.x,playerPos.y, playerDamage)
#ENEMY ----------------------------------------------------------------------------------
class Enemy:
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.random = random.randint(0,5)
        self.health = 0
        self.playerDamage = 10
        self.speed = 0
        self.vel = (player.pos - self.pos).normalize()
        self.radius = 10
        
    def update(self):
        self.pos += self.vel*self.speed
        
    def draw(self):
        if self.random == 0:
            pygame.draw.circle(screen, (0, 250, 0), (self.pos), self.radius)
            self.health = 100
            self.speed = 1

        elif self.random == 1:
            pygame.draw.circle(screen, (60, 200, 0), (self.pos), self.radius)
            self.health = 200
            self.speed = 0.9

        elif self.random == 2:
            pygame.draw.circle(screen, (120, 150, 0), (self.pos), self.radius)
            self.health = 400
            self.speed = 0.8
        
        elif self.random == 3:
            pygame.draw.circle(screen, (180, 100, 0), (self.pos), self.radius)
            self.health = 800
            self.speed = 0.7

        elif self.random == 4:
            pygame.draw.circle(screen, (240, 50, 0), (self.pos), self.radius)
            self.health = 2000
            self.speed = 0.3
    def collide8(self):
        if math.sqrt((mousePos[0]-self.pos.x)**2 + (mousePos[1]-self.pos.y)**2)<self.radius:
            self.health -= self.playerDamage
            print(self.health)
            return self.health
                
    
sebastiansmortalenemies = Enemy(enemyPos.x, enemyPos.y)
    

for i in range(30):
    enemy.append(Enemy(random.choice(xchoice), random.randint(0,800)))


    
#Main loop ___________________________________________________________________________________________
while Bye == False:
    time.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Bye = True
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            sebastiansmortalenemies.collide8()

        if event.type == pygame.MOUSEMOTION: #check if mouse moved
            mousePos = event.pos #refreshes mouse position
            
    
    sebastiansmortalenemies.update()
    
    #RENDER SECTION----------------------------------------------------------------------------
    screen.fill ((0,0,0))
    
    player.draw()
    sebastiansmortalenemies.draw()

    for i in range(len(enemy)):
        enemy[i].draw()
        enemy[i].update()
        enemy[i].collide8()

    
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(str(coins), 1 ,(255, 0, 0))
    screen.blit(text_surface, (0,0))
    pygame.display.flip() 

pygame.quit()
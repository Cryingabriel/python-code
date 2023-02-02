import pygame
import random


pygame.init()
pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
gameover = False
timer = 0
fire = random.randrange(100)
#player variables-----------------
xpos = 400
ypos = 750
meft = False
might = False
shoot = False
#enemy Class
class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isa = True
        self.direction = 1
    def move(self, time):
        if time % 800 == 0:
            self.ypos += 100
            self.direction *=-1
            return 0 #resets timer to 0
        #moves everytime the timer increases by 100
        if timer % 100==0:
            self.xpos+=50 *self.direction
            print("moving right)")
        return time
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 40, 40))
    def collide(self, BulletX, BulletY):
        if self.isa: #hit only alive aliens
            if BulletX > self.xpos:#check if the bulet is right of the left of the alien
                if BulletX < self.xpos + 40:#checks if the bullet is left of the right alien
                    if BulletY < self.ypos + 40:#checks if the bullet id above the alien
                        if BulletY > self.ypos:#checks if the bullet is below the alien
                            print("hit!")#testing
                            self.isa = False#set the alien to dead
                            return False#set the bullet to dead
        return True#otherwise keep bullet alive
class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isa = False
    def move(self, xpos, ypos):
        if self.isa == True: #only live shoot bullets
            self.ypos-=5 #move up when shot
        if self.ypos < 0:
            self.isa = False
            self.xpos = xpos
            self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))

#instantiate bullet object
bullet = Bullet(xpos+28, ypos)
group: list[Alien] = []#creat a list
for i in range (4): #handles the rows
    for y in range (9): #handle colums
        group.append(Alien(y*80+50, i*80+50))
Alfred = Alien(400, 400)#instantiating one
#WALLS
class wall:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
        self.numh = 0
    def draw(self):
        if self.numh == 0:
            pygame.draw.rect(screen, (250,250,0), (self.xpos, self.ypos, 30, 30))
        if self.numh == 1:
            pygame.draw.rect(screen, (150,150, 10), (self.xpos, self.ypos, 30, 30))
        if self.numh == 2:
            pygame.draw.rect(screen, (50,50,0), (self.xpos, self.ypos, 30, 30))
    def collide(self,BulletX, BulletY):
        if self.numh <= 3:#only happens when the target if below 3 hits
            if BulletX > self.xpos:
                if BulletX < self.xpos + 30:
                    if BulletY > self.ypos:
                        if BulletY < self.ypos + 30:
                            print("Wrong target!")
                            self.numh +=1
                            return self.numh
walls = []
Trump = wall(400, 670)
for k in range  (4):
    for l in range (2):
        for o in range (3):
            walls.append(wall(o*30+200*k+50, i*30+600))

class Missle:
    def __init__(self):
        self.xpos = -10
        self.ypos = -10
        self.isa = False
    def move(self, xpos, ypos):
        if self.isa == True: #only live shoot bullets
            self.ypos+=5 #move down when shot
        if self.ypos > 0:
            self.isa = False
            self.xpos = xpos
            self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))
missle = []
for m in range (100):
    missle.append(Missle())
#GAME LOOP _______________________________________
while not gameover:
    clock.tick(60)
    timer += 1
    #input section----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True #quit game if x is pressed in top corner
        
        if event.type == pygame.KEYDOWN:#-----------------------
            if event.key == pygame.K_LEFT:
                meft = True
            if event.key == pygame.K_RIGHT:
                might = True
            if event.key == pygame.K_SPACE:
                shoot = True
        
        if event.type == pygame.KEYUP:#---------------------------
            if event.key == pygame.K_LEFT:
                meft = False
            if event.key == pygame.K_RIGHT:
                might = False
            if event.key == pygame.K_SPACE:
                shoot = False
    #phyisics section------------------

    #check variables from the input section---------------
    if meft == True:
        vx =- 3
    else: vx = 0
    if might == True:
        vx =+ 3
    if shoot == True:
        bullet.isa = True
    if bullet.isa == True:
        bullet.move(xpos+28, ypos)
        if bullet.isa == True:
        #check for collision between bullet and enemy
            for i in range (len(group)):
                bullet.isa = group[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isa == False:
                    break
        #check for collision between bullet and walls
        if bullet.isa == True:   
            for i in range (len(walls)):
                bullet.isa = walls[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isa == False:
                    break
    else:
        bullet.xpos = xpos + 28
        bullet.ypos = ypos
    #update player position
    xpos += vx

    if fire < 2:
        p = random.randrage(len(group))
        if group[p].isa == True:
            for i in range (len(missle)):
                if missle[i].isa == False:
                    missle[i].isa == True
                    missle[i].xpos = group[i].xpos+5
                    missle[i].ypos = group[i].ypos+5

    #Render section-------------
    screen.fill((0, 0, 0))
    
    for i in range (len(group)):
        group[i].draw()
    for i in range (len(group)):
        group[i].move(timer)
    for i in range (len(walls)):
        walls[i].draw()
    bullet.draw()
    for i in range (len(missle)):
        missle[i].draw()
    pygame.draw.rect(screen, (200, 200, 100), (xpos, 750, 60, 20))
    pygame.display.flip()
#end game loop------------------

pygame.quit()

import pygame

pygame.init()
pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
gameover = False
timer = 0;
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
class bullet:
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
meep = bullet(xpos+28, ypos)
group = []#creat a list
for i in range (4): #handles the rows
    for y in range (9): #handle colums
        group.append(Alien(y*80+50, i*80+50))
Alfred = Alien(400, 400)#instantiating one


while not gameover:
    clock.tick(60)
    timer += 1
    #input section----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True #quit game if x is pressed in top corner
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                meft = True
            if event.key == pygame.K_RIGHT:
                might = True

        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                meft = False
            if event.key == pygame.K_RIGHT:
                might = False
        if event.type == pygame.K_SPACE:
            shoot = True
    #phyisics section------------------

    #check variables from the input section---------------
    if meft == True:
        vx =- 3
    else: vx = 0
    if might == True:
        vx =+ 3
    if shoot == True:
        meep.isa = True
    if meep.isa == True:
        meep.move(xpos+28, ypos)
    else:
        meep.xpos = xpos + 28
        meep.ypos = ypos
    #update player position
    xpos += vx
    #Render section-------------
    screen.fill((0, 0, 0))
    
    for i in range (len(group)):
        group[i].draw()
    for i in range (len(group)):
        group[i].move(timer)
    meep.draw()
    pygame.draw.rect(screen, (200, 200, 100), (xpos, 750, 60, 20))
    pygame.display.flip()
#end game loop------------------

pygame.quit()

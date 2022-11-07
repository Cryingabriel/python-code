import pygame
pygame.init()  
pygame.display.set_caption('breakout')  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
mexit = False

clock = pygame.time.Clock()
class brick:
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
    
    def draw(self):
        if self.alive is True:
            pygame.draw.rect(screen, (255,0, 255), (self.xpos, self.ypos, 50,20))
    def collide(self,x,y):
        if self.alive is True:
            if x+20>self.xpos and x<self.xpos+50 and y+20> self.ypos and y < self.ypos+20:
                self.alive = False
                return True
#______________________________
bob = brick(20,20)
ryan = brick(100,100)
alfred = brick(200,100)
#++++++++++++++++++++++++++++++
p1x = 400
p1y = 650
#+++++++++++++++
bx = 350
by = 250
bVx = 5
bVy = 5
#______________________________
while not mexit:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mexit = True
    #++++++++++++++++++++++
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        p1x-=10
    if keys [pygame.K_DOWN]:
        p1x+=10
    
    
    screen.fill((0,0,0))
    bob.draw()
    ryan.draw()
    alfred.draw()
    pygame.draw.rect(screen, (255,255,255), (p1x, p1y, 100, 20), 1)

    pygame.display.flip()

import pygame

pygame.init()
pygame.display.set_caption("targets")
screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()
gameover = False
timer = 0


class Target:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = 1
    def move(self,time):
        if time % 600 == 0:
            self.direction *=-1
        if timer % 1 == 0:
            self.xpos +=1 *self.direction
            return time
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.xpos, self.ypos), 120)
        pygame.draw.circle(screen, (255, 255, 255), (self.xpos+1, self.ypos+1), 90)
        pygame.draw.circle(screen, (0, 0, 255), (self.xpos+2, self.ypos+2), 60)
        pygame.draw.circle(screen, (255, 255, 255), (self.xpos+3, self.ypos+3), 30)
        pygame.draw.circle(screen, (255, 0, 0), (self.xpos+4, self.ypos+4), 15)

t1 = Target(120,150)
t2 = Target(120, 400)
t3 = Target(120, 650)
while gameover == False:
    timer += 1
    
    #Input section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True





    #Rendering section
    screen.fill((0, 0, 0))

    t1.draw()
    t1.move(timer)
    t2.draw()
    t2.move(timer)
    t3.draw()
    t3.move(timer)
    pygame.display.flip()


pygame.quit()
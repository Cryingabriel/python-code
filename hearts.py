import pygame #gaming module (aka library) 
import random
pygame.init() #initializes Pygame
pygame.display.set_caption("Valentine's day card") #sets the window title
clock = pygame.time.Clock
screen = pygame.display.set_mode((800, 800)) #creates game screen
font = pygame.font.Font('freesansbold.ttf', 32) #load font
img = pygame.image.load("dog.jpg").convert() #make sure this is saved to the same folder as your code
timer = 0
text1 = font.render('I Love You as a friend!', True, (250, 100, 100)) #numbers give color
text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200,150,150)) #this one includes background color
text3 = font.render('SEIZURE WARNING!', True, (250, 100, 100)) #numbers give color

card = False


class heart:
    def __init__(self, xpos, ypos):
        self.ypos = ypos
        self.xpos = xpos
        self.isa = True
    def move(self, time):
        if self.ypos >= 800:
            self.ypos = -50
        self.ypos += 1


    def draw(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        if self.isa == True:
            pygame.draw.circle(screen, (r,g,b), (self.xpos, self.ypos), 19) #top left circle
            pygame.draw.circle(screen, (r,g,b), (self.xpos+40, self.ypos), 19) #top right circle
            pygame.draw.polygon(screen, (r,g,b), ((self.xpos-20, self.ypos),(self.xpos+59, self.ypos), (self.xpos+20, self.ypos+50))) #triangle to form base


group: list[heart] = []#creat a list
for i in range (10): #handles the rows
    for y in range (10): #handle colums
        group.append(heart(y*80+50, i*80+50))


while card == False:
    timer +=1 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            card = True #quit game if x is pressed in top corner


    #Rendering
    w = random.randint(0,1) * 255
    screen.fill((w, w, w))
    for i in range (len(group)):
        group[i].draw()
    
    img.set_alpha(random.randint(0,1) * 255)
    text1.set_alpha(random.randint(0,1) * 255)
    text2.set_alpha(random.randint(0,1) * 255)
    text3.set_alpha(random.randint(0,1) * 255)
    screen.blit(img, (0, 400))#draw pic
    screen.blit(text1, (200, 100)) #numbers give position
    screen.blit(text2, (400, 300))
    screen.blit(text3, (0, 350))
    for i in range (len(group)):
        group[i].move(timer)
    pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)

pygame.quit()
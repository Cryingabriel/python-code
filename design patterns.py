# plant factory code: The Plant Factory code is a demonstration of the Factory design pattern in Python
# In this pattern, a central 'Factory' (the Plant Factory in our code)
# takes care of creating objects (plants, like shamrocks) without needing to specify the exact class of the object.
# It simplifies the object creation process, allowing the program to easily create and manage different types of plants,
# showcasing how the Factory design pattern provides a streamlined and flexible approach to object creation in programming.
# disclaimer: I used ChatGPT to help write parts of this code :)

import pygame
import random
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plant Factory")


# Plant base class---------------------------------------------------------------------------
class Plant:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y

    def draw(self, screen):
        raise NotImplementedError("You must implement the draw method.")

# Concrete Plant class - Shamrock-------------------------------------------------------------
class Shamrock(Plant):
    def draw(self, screen):
        #black outlines
        pygame.draw.circle(screen, (0,0,0), (self.xpos-20, self.ypos+20), 22,2) #leaves
        pygame.draw.circle(screen, (0,0,0), (self.xpos, self.ypos-10), 22,5)
        pygame.draw.circle(screen, (0,0,0), (self.xpos+20, self.ypos+20), 22,2)
        pygame.draw.rect(screen, (0,0,0), (self.xpos-10, self.ypos+20, 15, 50),2)#stem
        #green interiors
        pygame.draw.rect(screen, (0,150,85), (self.xpos-10, self.ypos+20, 15, 50))#stem
        pygame.draw.circle(screen, (0,151,0), (self.xpos-20, self.ypos+20), 20) #leaves
        pygame.draw.circle(screen, (85,150,0), (self.xpos, self.ypos-10), 20)
        pygame.draw.circle(screen, (85,150,85), (self.xpos+20, self.ypos+20), 20)

class yourmum(Plant):
    def draw(self, screen):
        #black outlines
        pygame.draw.circle(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.xpos-20, self.ypos+20), 10) #leaves

class sebastian(Plant):
    def draw(self, screen):
        #black outlines
        pygame.draw.rect(screen, (255,255,255), (self.xpos-10, self.ypos+20, 15, 50))#stem
        pygame.draw.circle(screen, (255,255,255), (self.xpos-20, self.ypos+20), 20) #leaves
        pygame.draw.circle(screen, (255,255,255), (self.xpos, self.ypos-10), 20)
        pygame.draw.circle(screen, (255,255,255), (self.xpos+20, self.ypos+20), 20)
# add more plant classes here...
class EVILsebastian(Plant):
    def draw(self, screen):
        #black outlines
        pygame.draw.rect(screen, (0,0,0), (self.xpos-10, self.ypos+20, 15, 50))#stem
        pygame.draw.circle(screen, (0,0,0), (self.xpos-20, self.ypos+20), 20) #leaves
        pygame.draw.circle(screen, (0,0,0), (self.xpos, self.ypos-10), 20)
        pygame.draw.circle(screen, (0,0,0), (self.xpos+20, self.ypos+20), 20)

# Factory class---------------------------------------------------------------------------------
class PlantFactory:
    def create_plant(self, plant_type, x, y):
        if plant_type == "shamrock":
            return Shamrock(x, y)
        elif plant_type == "yourmum":
            return yourmum(x1, y1)
        
        elif plant_type == "sebastian":
            return sebastian(x2, y2)
        # Add more plant type conditions here...
        elif plant_type == "EVILsebastian":
            return EVILsebastian(x3, y3)
        else:
            raise ValueError("Unknown plant type")

# Game setup
plant_factory = PlantFactory()
plants = []

# GAME LOOP----------------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # create a new shamrock at random positions
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(50, SCREEN_HEIGHT - 50)
    x1 = random.randint(50, SCREEN_WIDTH - 25)
    y1 = random.randint(100, SCREEN_HEIGHT - 25)
    x2 = random.randint(50, SCREEN_WIDTH - 13)
    y2 = random.randint(100, SCREEN_HEIGHT - 13)
    x3 = random.randint(50, SCREEN_WIDTH - 13)
    y3 = random.randint(100, SCREEN_HEIGHT - 13)
    plants.append(plant_factory.create_plant("shamrock", x, y))
    plants.append(plant_factory.create_plant("yourmum",x1,y1))
    plants.append(plant_factory.create_plant("sebastian",x2,y2))
    plants.append(plant_factory.create_plant("EVILsebastian",x3,y3))
    # render section------------------------
    screen.fill((0,0,0))  # Clear screen
    for plant in plants:
        plant.draw(screen)

    pygame.display.flip()
#end game loop-------------------------------------------------------------------------------------------
pygame.quit()
import pygame
from math import sin #this is so we don't have to say "math." in front of sin()

pygame.init()

gamescreen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Wave Beam")
clocky = pygame.time.Clock()
PlayingGame = True #variable used to quit game loop

#player position
xpos = 50
ypos = 75
#player speed
vx = 0
vy = 0
#variables to control wave beam
beam = False
beamx = 0
beamy = 0
beam2y = 0
beam2x = 0
angle = 0
A = 10
B = .2
C = 0
D = 0

a = 10
b = .4
c = 2
d = 0
#ship image load
ship = pygame.image.load("ship.png") #artwork credit: Mr. Mo
shipRect = ship.get_rect(topleft = (xpos, ypos))

#BEGIN GAME LOOP#################################################################
while PlayingGame:
  
  clocky.tick(60)
  
  events = pygame.event.get()
 
  for event in events:
    if event.type == pygame.QUIT:
      PlayingGame = False
      
  keys = pygame.key.get_pressed()
      
        
  if keys[pygame.K_LEFT]:
      vx=-5
  elif keys[pygame.K_RIGHT]:
      vx=5
  else:
      vx = 0

  if keys[pygame.K_DOWN]:
      vy =5
  elif keys[pygame.K_UP]:
      vy=-5
  else:
      vy=0

  #fire wave beam
  if keys[pygame.K_SPACE]:
      beam = True
  else:
      beam = False
        
  #PHYSICS SECTION-------------------------------------------------------------
  if beam is True:
      angle+=1 #rotate angle
      beamx = xpos+angle*5 #this handles how fast the beam moves to the right
      beamy = A*sin(B*(angle-C))+D #this handles the shape and size of the wave

      angle+=1 #rotate angle
      beam2x = xpos+angle*5  #this handles how fast the beam moves to the right
      beam2y = a*sin(b*(angle-c))+d #this handles the shape and size of the wave
  else:
      angle = 0
        
  #update player position by adding velocity to position      
  xpos += vx
  ypos += vy
  shipRect = ship.get_rect(topleft = (xpos, ypos))
  
  
  #RENDER SECTION-------------------------------------------------------------      
  #gamescreen.fill((0,0,0))
  
  #draw spaceship
  gamescreen.blit(ship, shipRect)
  
  #draw beam when fired
  if beam is True:
      pygame.draw.circle(gamescreen, (200, 0, 100), (beamx+10, beamy+ypos+20), 5)
      pygame.draw.circle(gamescreen, (255, 255, 255), (beam2x+10, beam2y+ypos+20), 5)
      
  pygame.display.flip()




  #END GAME LOOP#################################################################
pygame.quit()
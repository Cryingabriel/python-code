import pygame
import random
from pygame.math import Vector2
from random import randrange as rr
import math
import time
pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption("Single particle movement")
clock = pygame.time.Clock()
pygame.mixer.init()
SAO = pygame.mixer.Sound("C:/Users/734540/Documents/GitHub/python-code/1-30-24/1.mp3")


class Particles():
	def __init__(self, xpos, ypos,amount):
		self.amount = amount
		self.pos = []
		self.xvel = []
		self.yvel = []
		self.speed = 1.2
		self.magnitude = []
		self.nxvel = []
		self.nyvel = []
		self.size = []
		for i in range(self.amount):
			self.pos.append(Vector2(xpos,ypos))
			self.xvel.append(random.uniform(-10,10))
			self.yvel.append(random.uniform(-10,10))
			self.magnitude.append(math.sqrt(self.xvel[i] ** 2 + self.yvel[i] ** 2))
			self.nxvel.append(0)
			self.nyvel.append(0)
			self.size.append(2)

	def update(self):
		for num in range(self.amount):
			self.move(num)
			self.draw(num)
			
	def move(self,num):
		self.pos[num].x += self.xvel[num]
		self.pos[num].y += self.yvel[num]
		self.size[num] += ((abs(self.xvel[num])+abs(self.yvel[num]))/2)/50
		if self.size[num] < 1:
			self.size[num] = 2
		if self.pos[num].x < 0 or self.pos[num].x > 900 or self.pos[num].y < 0 or self.pos[num].y > 900:
			self.xvel[num] = random.uniform(-10,10)
			self.yvel[num] = random.uniform(-10,10)
			self.pos[num].x = 450
			self.pos[num].y = 450
			self.size[num] = 2
			
			
		#self.magnitude[num] = math.sqrt(self.xvel[num]**2 + self.yvel[num] ** 2)

		if self.magnitude[num] != 0:
			self.nyvel[num] = self.speed *  self.yvel[num] / self.magnitude[num]
			self.nxvel[num] = self.speed *  self.xvel[num] / self.magnitude[num]
			
        
	
			
        
	
        

	def draw(self,num):
		pygame.draw.circle(screen, (rr(0,255), rr(0,255), rr(0,255)), (self.pos[num].x,self.pos[num].y), self.size[num])



particles = Particles(450,450,500)
pygame.mixer.Sound.play(SAO)
#time.sleep(2)
#pygame.mixer.Sound.play(SAO)
#time.sleep(2)
#pygame.mixer.Sound.play(SAO)
#time.sleep(2)
#pygame.mixer.Sound.play(SAO)
#time.sleep(2)
#pygame.mixer.Sound.play(SAO)
#time.sleep(2)
#pygame.mixer.Sound.play(SAO)
#time.sleep(2)
#pygame.mixer.Sound.play(SAO)
while True:
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			break
		

   

	#1.comment out screen.fill and youll see a reference
	#screen.fill((rr(0,55),rr(0,55),rr(0,55)))

	particles.update()
	pygame.display.flip()

pygame.quit()





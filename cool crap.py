import pygame
import random
from pygame.math import Vector2
from random import randrange as rr

pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption("Single particle movement")
clock = pygame.time.Clock()


class Particles():
	def __init__(self, xpos, ypos,amount):
		self.amount = amount
		self.pos = []
		self.xvel = []
		self.yvel = []
		for i in range(self.amount):
			self.pos.append(Vector2(xpos,ypos))
			self.xvel.append(random.uniform(-1,1))
			self.yvel.append(random.uniform(-1,1))

	def update(self):
		for num in range(self.amount):
			self.move(num)
			self.draw(num)
			
	def move(self,num):
		self.pos[num].x += self.xvel[num]
		self.pos[num].y += self.yvel[num]
		if self.pos[num].x < 0 or self.pos[num].x > 900:
			self.xvel[num] = random.uniform(-1,1)
			self.pos[num].x = 450
		if self.pos[num].y < 0 or self.pos[num].y > 900:
			self.yvel[num] = random.uniform(-1,1)
			self.pos[num].y = 450

	def draw(self,num):
		pygame.draw.circle(screen, (rr(0,255), rr(0,255), rr(0,255)), (self.pos[num].x,self.pos[num].y), 5)



particles = Particles(450,450,100)

while True:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			break
		

   

	
	screen.fill((0,0,0))

	particles.update()
	pygame.display.flip()

pygame.quit()





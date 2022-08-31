import pygame #puts pygame in 
pygame.init #initialize pygame

screen = pygame.display.set_mode((800,800)) #creates game screen

pygame.draw.rect(screen, (255,0,0), (100,100,100,100))
pygame.draw.polygon(screen, (0,255,0), ((150,50), (200,100),(100,100)))
pygame.display.flip()
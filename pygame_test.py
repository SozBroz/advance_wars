#Importing the library
import pygame
from image_index import fetch_picture_symbol_dict  
# Initializing Pygame
picture_symbol_dict = fetch_picture_symbol_dict()


pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((400,300))
  
# Initialing Color
color = (255,0,0)
  
# Drawing Rectangle
for a in range(0,5):
	for b in range(0,5):
		surface.blit(pygame.image.load("images/" + picture_symbol_dict[str(a * 10 + b + 1)]), (a*16,b*16))
pygame.display.flip()

input()
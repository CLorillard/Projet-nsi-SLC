import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("image/background.jpg").convert()
fenetre.blit(fond, (0,0))


#Rafraîchissement de l'écran
pygame.display.flip()



#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True

while continuer:
	for event in pygame.event.get():  
		if event.type == QUIT:     
			continuer = False
pygame.quit()

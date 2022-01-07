import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("image/background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage 
perso = pygame.image.load("image/perso.jpg").convert()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)


#Rafraîchissement de l'écran
pygame.display.flip()



#BOUCLE INFINIE
continuer = True

while continuer:
    for event in pygame.event.get():  
        if event.type == QUIT:     
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:	#Si "flèche bas"
            #On descend le perso
                position_perso = position_perso.move(0,3)
            
            
        fenetre.blit(fond, (0,0))	
        fenetre.blit(perso, position_perso)
        #Rafraichissement
        pygame.display.flip()
            
            
        

pygame.quit()

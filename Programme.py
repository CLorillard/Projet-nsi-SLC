import pygame
import os
from pygame.locals import *

pygame.init()

#ouverture de la fenetre pygame
WIDHT, HEIGHT = 1000, 700
FENETRE = pygame.display.set_mode((WIDHT, HEIGHT))  #définition taille de la fenetre
pygame.display.set_caption("CANDY MAYZE")    #nom de la fenetre

#Chargement du fond
FOND_1 = pygame.image.load("image/background.jpg").convert()
FOND = pygame.transform.scale(FOND_1, (WIDHT, HEIGHT))

PERSO_WIDHT, PERSO_HEIGHT = (100, 140) #dimension perso

DIST = 1  #variable pour ajout lors déplacement personnage

#Chargement du personnage
PERSONNAGE = pygame.image.load(os.path.join("image","perso.png"))
PERSO = pygame.transform.scale(PERSONNAGE, (PERSO_WIDHT, PERSO_HEIGHT))    #redimensionnage du perso
#si rotation voulue utilier pygame.transform.rotate()

NOTICE_1 = pygame.image.load("image/regles.png").convert() #importation de l'image NOTICE
NOTICE =  pygame.transform.scale(NOTICE_1, (700,300))



#variables couleurs
WHITE = (255, 255, 255)
color_light = (170,170,170)
color_dark = (100,100,100)

smallfont = pygame.font.SysFont('arial',35) #police et taille de texte 
text = smallfont.render('?' , True , WHITE) # point d'interrogation

FPS = 60 #pour pouvoir definir nombre de fois que la boucle tourne par seconde

def perso_mouvement(keys_pressed,perso):
    if keys_pressed[pygame.K_LEFT] and perso.x - DIST > 0:  #si flèche gauche pressée et ne sort pas du cadre
        perso.x -= DIST  #perso se déplace à gauche
    if keys_pressed[pygame.K_RIGHT]and perso.x + DIST < WIDHT - PERSO_WIDHT:  #si flèche droite pressée et ne sort pas du cadre
        perso.x += DIST   #perso se déplace  à droite
    if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:   #si flèche haut pressée et ne sort pas du cadre
        perso.y -= DIST    #perso se déplace vers le haut
    if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:   #si flèche bas pressée et ne sort pas du cadre
        perso.y += DIST    #perso se déplace vers le bas



    
    

def main():
    perso = pygame.Rect(100, 300, PERSO_WIDHT, PERSO_HEIGHT) #coordonnées du perso avec la fonction rect
    clock = pygame.time.Clock()
    run = True
    aide= False
    while run:
        FENETRE.blit(FOND, (0,0)) #affichage du fond
        if aide:
            FENETRE.blit(NOTICE,(50,0))
        for event in pygame.event.get(): #pour les actions effectués dans la fenetre pygame
            if event.type == pygame.QUIT:    #si croix rouge
                run = False    # alors run = 0 donc sort de la boucle while
                
            if event.type == pygame.MOUSEBUTTONDOWN: #si on appuie sur la souris
                if WIDHT-30 <= mouse[0] <= WIDHT-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40: #position de la souris sur l'ecran
                    if aide== False:#si l'aide n'est pas ouverte
                        aide=True #ouvre l'aide
                    else:
                        aide=False#n'ouvre pas l'aide ou la ferme
                
        mouse = pygame.mouse.get_pos() #coordonnées de la souris
        if WIDHT-30 <= mouse[0] <= WIDHT-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40:
            pygame.draw.rect(FOND,color_light,[WIDHT-30,HEIGHT-690,40,40]) #crée un rectangle gris clair si on passe la souris dessus
          
        else:
            pygame.draw.rect(FOND,color_dark,[WIDHT-30,HEIGHT-690,40,40]) #crée un rectangle gris foncé si la souris n'est pas dessus
        FENETRE.blit(text , (WIDHT-30,HEIGHT-690))

        keys_pressed = pygame.key.get_pressed()  #définition variable quand une key est appuyée

        perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
        FENETRE.blit(PERSO, (perso.x, perso.y))   #affichage du perso a un endroit preci sur fenetre

        
        
        pygame.display.update()   # rafraichissement de la page
        
    pygame.quit()   #fermeture propre de la fenêtre


if __name__ == "__main__":
    main()

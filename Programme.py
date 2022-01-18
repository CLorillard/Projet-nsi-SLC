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

WHITE = (255, 255, 255)

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

def draw_window(perso):
    FENETRE.blit(FOND, (0,0)) #affichage du fond
    FENETRE.blit(PERSO, (perso.x, perso.y))   #affichage du perso a un endroit preci sur fenetre
    pygame.display.update()   # rafraichissement de la page

def main():
    perso = pygame.Rect(100, 300, PERSO_WIDHT, PERSO_HEIGHT) #coordonnées du perso avec la fonction rect

    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    #si croix rouge
                run = False    # alors run = 0 donc sort de la boucle while

        keys_pressed = pygame.key.get_pressed()  #définition variable quand une key est appuyée

        perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso

        draw_window(perso) #appel fonction qui projette du blanc + perso

    pygame.quit()   #fermeture propre de la fenêtre


if __name__ == "__main__":
    main()

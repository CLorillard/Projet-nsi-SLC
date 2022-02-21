import pygame
import os
from pygame.locals import *

pygame.init()
pygame.mixer.init()

#ouverture de la fenetre pygame
WIDTH, HEIGHT = 1000, 700
FENETRE = pygame.display.set_mode((WIDTH, HEIGHT))  #définition taille de la fenetre
pygame.display.set_caption("CANDY MAYZE")    #nom de la fenetre

#Chargement des fonds
FOND_1 = pygame.image.load("image/background.jpg").convert()
FOND = pygame.transform.scale(FOND_1, (WIDTH, HEIGHT))

FOND2_1=pygame.image.load("image/FOND2.jpg").convert()
FOND2 = pygame.transform.scale(FOND2_1, (WIDTH, HEIGHT))

PERSO_WIDTH, PERSO_HEIGHT = (100, 140) #dimension perso

DIST = 1  #variable pour ajout lors déplacement personnage

#chargement de la musique
MUSIQUE = pygame.mixer.music.load("Musique/musique.wav")

#Chargement du personnage
PERSONNAGE = pygame.image.load(os.path.join("image","perso.png"))
PERSO = pygame.transform.scale(PERSONNAGE, (PERSO_WIDTH, PERSO_HEIGHT))    #redimensionnage du perso
#si rotation voulue utilier pygame.transform.rotate()

NOTICE_1 = pygame.image.load("image/regles.png").convert() #importation de l'image NOTICE
NOTICE =  pygame.transform.scale(NOTICE_1, (700,300))

NIVEAU_1 = pygame.image.load("image/niveau1.png").convert_alpha() #importation de l'image niveau1
NIVEAU1 =  pygame.transform.scale(NIVEAU_1, (200,350))

NIVEAU_2 = pygame.image.load("image/niveau2.jpg").convert_alpha() #importation de l'image niveau2
NIVEAU2 =  pygame.transform.scale(NIVEAU_2, (200,350))

NIVEAU_3 = pygame.image.load("image/niveau3.png").convert_alpha() #importation de l'image niveau3
NIVEAU3 =  pygame.transform.scale(NIVEAU_3, (200,350))

TOUTDROIT_1=pygame.image.load("image/toutdroit.jpg").convert()
TOUTDROIT=pygame.transform.scale(TOUTDROIT_1, (WIDTH, HEIGHT))

INTERSECTION2_1=pygame.image.load("image/deuxchemin.jpg").convert()
INTERSECTION2=pygame.transform.scale(INTERSECTION2_1, (WIDTH, HEIGHT))

CULDESAC_1=pygame.image.load("image/cusdesac.jpg").convert()
CULDESAC=pygame.transform.scale(CULDESAC_1, (WIDTH, HEIGHT))

GAMEOVER_1=pygame.image.load("image/gameover.jpg").convert()
GAMEOVER=pygame.transform.scale(GAMEOVER_1, (WIDTH, HEIGHT))




#variables couleurs
WHITE = (255, 255, 255)
color_light = (130,170,210)
color_dark = (100,125,190)

smallfont = pygame.font.SysFont('arial',35) #police et taille de texte
text = smallfont.render('?' , True , WHITE) # point d'interrogation


FPS = 60 #pour pouvoir definir nombre de fois que la boucle tourne par seconde

def perso_mouvement(keys_pressed,perso):
    if keys_pressed[pygame.K_LEFT] and perso.x - DIST > 0:  #si flèche gauche pressée et ne sort pas du cadre
        perso.x -= DIST  #perso se déplace à gauche
    if keys_pressed[pygame.K_RIGHT]and perso.x + DIST < WIDTH - PERSO_WIDTH:  #si flèche droite pressée et ne sort pas du cadre
        perso.x += DIST   #perso se déplace  à droite
    if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:   #si flèche haut pressée et ne sort pas du cadre
        perso.y -= DIST    #perso se déplace vers le haut
    if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:   #si flèche bas pressée et ne sort pas du cadre
        perso.y += DIST    #perso se déplace vers le bas
    if WIDTH-500 <= perso.x <= WIDTH-500+100 and HEIGHT-690 <= perso.y <= HEIGHT-690+100:
        milieu()

def gauche():
    FENETRE.blit(TOUTDROIT, (0,0))

def droite():
    FENETRE.blit(TOUTDROIT, (0,0))

def milieu():
    FENETRE.blit(TOUTDROIT, (0,0))

def intersection2():
    FENETRE.blit(INTERSECTION2, (0,0))

def culdesac():
    FENETRE.blit(CULDESAC, (0,0))

compte=1
def niveau1bis():
    if milieu() or droite() or gauche():
        compte=compte+1
    if culdesac():
        compte=compte-compte

def gagne():
    if compte==10:
        FENETRE.blit(MAISON, (0,0))

def perdu():
    if compte==0:
        FENETRE.blit(GAMEOVER, (0,0))


def niveau1():
    milieu()
    milieu()
    for k in range(6):
        intersection2()
        if droite():
            milieu()
        if gauche():
            milieu()
            culdesac()
        milieu()
        milieu()
        gagne()


def main():
    perso = pygame.Rect(450, 600, PERSO_WIDTH, PERSO_HEIGHT) #coordonnées du perso avec la fonction rect
    clock = pygame.time.Clock()
    pygame.mixer.music.play(-1,0.0)
    run = True
    aide= False
    jouer=False
    while run:

        FENETRE.blit(FOND, (0,0)) #affichage du fond
        for event in pygame.event.get(): #pour les actions effectués dans la fenetre pygame
            if event.type == pygame.QUIT:    #si croix rouge
                run = False    # alors run = 0 donc sort de la boucle while

            if event.type == pygame.MOUSEBUTTONDOWN: #si on appuie sur la souris
                if WIDTH-30 <= mouse[0] <= WIDTH-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40: #position de la souris sur l'ecran
                    if aide== False:#si l'aide n'est pas ouverte
                        aide=True #ouvre l'aide
                    else:
                        aide=False#n'ouvre pas l'aide ou la ferme
                if WIDTH-750 <= mouse[0] <= WIDTH-750+500 and HEIGHT-400 <= mouse[1] <= HEIGHT-400+200:
                    if jouer==False:
                        jouer=True
                if WIDTH-200 <= mouse[0] <= WIDTH-200+50 and HEIGHT-230 <= mouse[1] <= HEIGHT-230+500:
                    niveau1()


        mouse = pygame.mouse.get_pos() #coordonnées de la souris
        if WIDTH-30 <= mouse[0] <= WIDTH-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40:
            pygame.draw.rect(FOND,color_light,[WIDTH-40,HEIGHT-690,40,40]) #crée un rectangle gris clair si on passe la souris dessus
            FENETRE.blit(text , (WIDTH-30,HEIGHT-690))

        else:
            pygame.draw.rect(FOND,color_dark,[WIDTH-40,HEIGHT-690,40,40]) #crée un rectangle gris foncé si la souris n'est pas dessus
            FENETRE.blit(text , (WIDTH-30,HEIGHT-690))


        if aide:
            FENETRE.blit(NOTICE,(50,0))

        if jouer:
            FENETRE.blit(FOND2, (0,0))
            keys_pressed = pygame.key.get_pressed()  #définition variable quand une key est appuyée

            perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
            FENETRE.blit(PERSO, (perso.x, perso.y))   #affichage du perso a un endroit preci sur fenetre
            FENETRE.blit(NIVEAU1, (200,230))
            FENETRE.blit(NIVEAU2, (400,250))
            FENETRE.blit(NIVEAU3, (600,260))





        pygame.display.update()   # rafraichissement de la page




    pygame.quit()   #fermeture propre de la fenêtre



if __name__ == "__main__":
    main()
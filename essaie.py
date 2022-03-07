import pygame
import os
import time
from pygame.locals import *

pygame.init()
pygame.mixer.init()


#ouverture de la fenetre pygame
WIDTH, HEIGHT = 1000, 700
FENETRE = pygame.display.set_mode((WIDTH, HEIGHT))  #définition taille de la fenetre
pygame.display.set_caption("CANDY MAZE")    #nom de la fenetre

#Chargement des fonds
FOND_1 = pygame.image.load("image/background.jpg").convert()
FOND = pygame.transform.scale(FOND_1, (WIDTH, HEIGHT))

FOND2_1=pygame.image.load("image/FOND2.jpg").convert()
FOND2 = pygame.transform.scale(FOND2_1, (WIDTH, HEIGHT))

che2_1=pygame.image.load("image/deuxchemin.jpg").convert()
che2 = pygame.transform.scale(che2_1, (WIDTH, HEIGHT))

toutdroit_1=pygame.image.load("image/toutdroit.jpg").convert()
toutdroit = pygame.transform.scale(toutdroit_1, (WIDTH, HEIGHT))

PERSO_WIDTH, PERSO_HEIGHT = (100, 140) #dimension perso

DIST = 1  #variable pour ajout lors déplacement personnage

#chargement de la musique
#MUSIQUE = pygame.mixer.music.load("musique.wav")

#Chargement du personnage
PERSONNAGE = pygame.image.load(os.path.join("image", "perso.png"))
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



    

def main():
    perso = pygame.Rect(450, 600, PERSO_WIDTH, PERSO_HEIGHT) #coordonnées du perso avec la fonction rect
    clock = pygame.time.Clock()
    #pygame.mixer.music.play(-1,0.0)
    run = True
    aide= False
    jouer=False
    niveau1=False
    map_gauche = 0
    map_droite = 0
    map_haut = 0
    map_bas = 0

    while run:
        
        FENETRE.blit(FOND, (0,0)) #affichage du fond
        for event in pygame.event.get(): #pour les actions effectués dans la fenetre pygame
            if event.type == pygame.QUIT:    #si croix rouge
                run = False    # alors run = 0 donc sort de la boucle while
                
            if event.type == pygame.MOUSEBUTTONDOWN: #si on appuie sur la souris
                print(mouse[0], mouse[1])
                if WIDTH-30 <= mouse[0] <= WIDTH-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40: #position de la souris sur l'ecran
                    if aide== False:#si l'aide n'est pas ouverte
                        aide=True #ouvre l'aide
                    else:
                        aide=False#n'ouvre pas l'aide ou la ferme



                if WIDTH-750 <= mouse[0] <= WIDTH-750+500 and HEIGHT-400 <= mouse[1] <= HEIGHT-400+200:
                    if jouer==False:
                        jouer=True
                
                
                
                if WIDTH-900 <= mouse[0] <= WIDTH-900+250 and HEIGHT-400 <= mouse[1] <= HEIGHT-400+200:
                    print("love")
                    if niveau1==False:
                        niveau1=True

            
        mouse = pygame.mouse.get_pos() #coordonnées de la souris
        if WIDTH-30 <= mouse[0] <= WIDTH-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40:
            pygame.draw.rect(FOND,color_light,[WIDTH-40,HEIGHT-690,40,40]) #crée un rectangle gris clair si on passe la souris dessus
            FENETRE.blit(text , (WIDTH-30,HEIGHT-690))

        else:
            pygame.draw.rect(FOND,color_dark,[WIDTH-40,HEIGHT-690,40,40]) #crée un rectangle gris foncé si la souris n'est pas dessus
            FENETRE.blit(text , (WIDTH-30,HEIGHT-690))
#300 329
        
        if aide:
            FENETRE.blit(NOTICE,(50,0))
            
    
        if jouer:
            if niveau1:
                FENETRE.blit(toutdroit, (0, 0))
                keys_pressed = pygame.key.get_pressed() 
                perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                FENETRE.blit(PERSO, (perso.x, perso.y))
        
                if perso.x - DIST <= 0 :
                    map_gauche += 1
                    perso.x = perso.x + 900
                elif perso.x + DIST < WIDTH - PERSO_WIDTH:
                    map_droite+=1
                elif perso.y - DIST > 0:
                    map_haut+=1
                elif perso.y + DIST < HEIGHT - PERSO_HEIGHT:
                    map_bas+=1
                #print(map_gauche)




                if map_gauche ==1:
                    FENETRE.blit(che2, (0, 0))
                elif map_gauche ==2:
                    FENETRE.blit(toutdroit, (0, 0))
                keys_pressed = pygame.key.get_pressed() 
                perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                FENETRE.blit(PERSO, (perso.x, perso.y))



            else:
            
                
                FENETRE.blit(FOND2, (0, 0))
                 #définition variable quand une key est appuyée
                FENETRE.blit(NIVEAU1, (200,230))
                FENETRE.blit(NIVEAU2, (400,250))
                FENETRE.blit(NIVEAU3, (600,260))

    
    
        pygame.display.update()   # rafraichissement de la page
        
        
            
        
    pygame.quit()   #fermeture propre de la fenêtre



if __name__ == "__main__":
    main()
    
'''pygame.init()
WIDHT, HEIGHT = 1000, 700
FENETRE = pygame.display.set_mode((WIDHT, HEIGHT))
run = True
images=[]
images.append(pygame.image.load("image/cusdesac.jpg").convert())
images.append(pygame.image.load("image/toutdroit.jpg").convert())
images.append(pygame.image.load("image/deuxchemin.jpg").convert())
images.append(pygame.image.load("image/arrivee.jpg").convert())
while run:
    for event in pygame.event.get(): #pour les actions effectués dans la fenetre pygame
        if event.type == pygame.QUIT:    #si croix rouge
            run = False
    FENETRE.blit(images[0],(0,0))
    
    pygame.display.update()
pygame.quit()   #fermeture propre de la fenêtre'''

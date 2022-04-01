import pygame, time, os, random

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

game_over_1= pygame.image.load("image/gameover.jpg").convert()
game_over = pygame.transform.scale(game_over_1, (WIDTH, HEIGHT))

cul_de_sac_1= pygame.image.load("image/cusdesac.jpg").convert()
cul_de_sac_2=pygame.transform.rotate(cul_de_sac_1,+90)
cul_de_sac = pygame.transform.scale(cul_de_sac_2, (WIDTH, HEIGHT))

FOND2_1=pygame.image.load("image/FOND2.jpg").convert()
FOND2 = pygame.transform.scale(FOND2_1, (WIDTH, HEIGHT))

FINISH_1=pygame.image.load("image/maison.jpg").convert()
FINISH= pygame.transform.scale(FINISH_1, (WIDTH, HEIGHT))

che2_1=pygame.image.load("image/deuxchemin.jpg").convert()
che2_2= pygame.transform.rotate(che2_1,90)
che2 = pygame.transform.scale(che2_2, (WIDTH, HEIGHT))

toutdroit_1=pygame.image.load("image/toutdroit.jpg").convert()
toutdroit_2=pygame.transform.rotate(toutdroit_1,-90)
toutdroit = pygame.transform.scale(toutdroit_2, (WIDTH, HEIGHT))

toutdroit2_1=pygame.image.load("image/toutdroit2.jpg").convert()
toutdroit2_2=pygame.transform.rotate(toutdroit2_1,+90)
toutdroit2 = pygame.transform.scale(toutdroit2_2, (WIDTH, HEIGHT))

droit_1=pygame.image.load("image/droit.jpg").convert()
droit = pygame.transform.scale(droit_1, (WIDTH, HEIGHT))

PERSO_WIDTH, PERSO_HEIGHT = (100, 140) #dimension perso

DIST = 2  #variable pour ajout lors déplacement personnage

#chargement de la musique
MUSIQUE = pygame.mixer.music.load("Musique/musique.wav")

#Chargement du personnage
PERSONNAGE = pygame.image.load(os.path.join("image", "perso.png"))
PERSO = pygame.transform.scale(PERSONNAGE, (PERSO_WIDTH, PERSO_HEIGHT))    #redimensionnage du perso
#si rotation voulue utilier pygame.transform.rotate()

NOTICE_1 = pygame.image.load("image/regles.png").convert() #importation de l'image NOTICE
NOTICE =  pygame.transform.scale(NOTICE_1, (700,300))

NIVEAU_1 = pygame.image.load("image/niveau1.png").convert_alpha() #importation de l'image niveau1
NIVEAU1 =  pygame.transform.scale(NIVEAU_1, (200,350))

NIVEAU_2 = pygame.image.load("image/niveau2.png").convert_alpha() #importation de l'image niveau2
NIVEAU2 =  pygame.transform.scale(NIVEAU_2, (200,350))

NIVEAU_3 = pygame.image.load("image/niveau3.png").convert_alpha() #importation de l'image niveau3
NIVEAU3 =  pygame.transform.scale(NIVEAU_3, (200,350))

#variables couleurs
WHITE = (255, 255, 255)
color_light = (130,170,210)
color_dark = (100,125,190)

smallfont = pygame.font.SysFont('arial',35) #police et taille de texte 
text = smallfont.render('?' , True , WHITE) # point d'interrogation


map_1 = []
for i in range(3):
    map_1.append(random.choice([1, 2]))
    
map_2 = []
for i in range (7):
    map_2.append(random.choice([1,2]))
    
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
    #clock = pygame.time.Clock()
    #pygame.mixer.music.play(-1,0.0)
    run = True
    aide= False
    jouer=False
    niveau1=False
    niveau2=False
    niveau3=False
    map_gauche = 0
    map_droite = 0
    map_haut = 0
    map_bas = 0
    culdesac = 0
    i=0
    game_over_45 = 0
    
            
    while run:
        
            
        FENETRE.blit(FOND, (0,0)) #affichage du fond
        for event in pygame.event.get(): #pour les actions effectués dans la fenetre pygame
            if event.type == pygame.QUIT:    #si croix rouge
                run = False    # alors run = 0 donc sort de la boucle while
                
            if event.type == pygame.MOUSEBUTTONDOWN: #si on appuie sur la souris
                #(mouse[0], mouse[1])
                if WIDTH-30 <= mouse[0] <= WIDTH-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40: #position de la souris sur l'ecran
                    if aide== False:#si l'aide n'est pas ouverte
                        aide=True #ouvre l'aide
                    else:
                        aide=False#n'ouvre pas l'aide ou la ferme


        


                
                if WIDTH-825 <= mouse[0] <= WIDTH-825+175 and HEIGHT-450 <= mouse[1] <= HEIGHT-450+300 and jouer:
                    print("love")
                    if niveau1==False:
                        niveau1=True

                if WIDTH-600 <= mouse[0] <= WIDTH-600+175 and HEIGHT-450 <= mouse[1] <= HEIGHT-450+300 and jouer:
                    print("aime")
                    if niveau2==False:
                        niveau2=True


                if WIDTH-375 <= mouse[0] <= WIDTH-425+175 and HEIGHT-450 <= mouse[1] <= HEIGHT-450+300 and jouer:
                    print("coeur")
                    if niveau3==False:
                        niveau3=True

                if WIDTH-750 <= mouse[0] <= WIDTH-750+500 and HEIGHT-400 <= mouse[1] <= HEIGHT-400+200:
                    if jouer==False:
                        jouer=True
       
            
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

            if niveau1:
                
                print(map_1)
                print(map_droite)
                print(map_gauche)
                print(i)
                print(niveau1)
                FENETRE.blit(droit, (0, 0))
                keys_pressed = pygame.key.get_pressed() 
                perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                FENETRE.blit(PERSO, (perso.x, perso.y))
                if perso.y - DIST <= 0:
                    if WIDTH-950 <= perso.x <= WIDTH-950+275 and map_haut:
                        map_gauche+=1

                    elif WIDTH-525 <= perso.x <= WIDTH-525+275 and map_haut:
                        map_droite+=1
                    map_haut+=1
                    perso.y = perso.y + 700

                if map_haut ==1:
                    FENETRE.blit(che2, (0, 0))
                elif map_haut ==2:
                    if map_gauche == 1 and map_1[i]==1:
                        #print(map)
                        print("c d s 1")
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1
                    elif map_gauche == 1 and map_1[i]==2:
                        FENETRE.blit(toutdroit2, (0, 0))
                        print("t 1")
                    elif map_droite == 1 and map_1[i]==1:
                        FENETRE.blit(toutdroit, (0,0))
                        print("t 2")
                    elif map_droite == 1 and map_1[i]==2:
                        print("c d s 2")
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1
                elif culdesac == 1:
                    print(map_droite)
                    FENETRE.blit(game_over, (0, 0))
                    game_over_45 = 1
                    i=0
                    print(niveau1)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if WIDTH-600 <= mouse[0] <= WIDTH-600+175 and HEIGHT-450 <= mouse[1] <= HEIGHT-450+300 :
                                game_over_45 = 0
                                map_gauche = 0
                                map_droite = 0
                                map_haut = 0
                                map_bas = 0
                                culdesac = 0
                                i = 0
                        elif event.type == pygame.KEYDOWN:
                            if event.key == K_RETURN:
                                niveau1 = False
                                game_over_45 = 0
                                map_gauche = 0
                                map_droite = 0
                                map_haut = 0
                                map_bas = 0
                                culdesac = 0
                                i = 0
                                
                elif game_over_45 == 1 :
                    FENETRE.blit(game_over, (0, 0))
                    
                else :
                    if map_haut != 0:
                        i += 1
                        map_haut = 0
                        map_droite = 0
                        map_gauche = 0 
                            
                if i == 3 :
                    FENETRE.blit(FINISH, (0,0))
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            niveau1 = False
                            i = 0       
                            print(i) 
                            map_gauche = 0
                            map_droite = 0
                            map_haut = 0
                            map_bas = 0
                            culdesac = 0
                            map_1.clear()
                            print(map_1)
                            for i in range(3):
                                map_1.append(random.choice([1, 2]))
                            i = 0    
                                
                elif i > 3 :
                    FENETRE.blit(FINISH, (0,0))
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            niveau1 = False
                            i = 0       
                            print(i) 
                            map_gauche = 0
                            map_droite = 0
                            map_haut = 0
                            map_bas = 0
                            culdesac = 0
                            map_1.clear()
                            print(map_1)
                            for i in range(3):
                                map_1.append(random.choice([1, 2]))
                            i = 0
                    

                    #FENETRE.blit(che2, (0, 0))

                keys_pressed = pygame.key.get_pressed() 
                perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                FENETRE.blit(PERSO, (perso.x, perso.y))
            elif niveau2:
                
                
                print(map_2)
                FENETRE.blit(droit, (0, 0))
                keys_pressed = pygame.key.get_pressed() 
                perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                FENETRE.blit(PERSO, (perso.x, perso.y))
                if perso.y - DIST <= 0:
                    if WIDTH-950 <= perso.x <= WIDTH-950+275 and map_haut:
                        map_gauche+=1

                    elif WIDTH-525 <= perso.x <= WIDTH-525+275 and map_haut:
                        map_droite+=1
                    map_haut+=1
                    perso.y = perso.y + 700

                if map_haut ==1:
                    FENETRE.blit(che2, (0, 0))
                elif map_haut ==2:
                    if map_gauche == 1 and map_2[i]==1:
                        #print(map)
                        print("c d s 1")
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1
                    elif map_gauche == 1 and map_2[i]==2:
                        FENETRE.blit(toutdroit2, (0, 0))
                        print("t 1")
                    elif map_droite == 1 and map_2[i]==1:
                        FENETRE.blit(toutdroit, (0,0))
                        print("t 2")
                    elif map_droite == 1 and map_2[i]==2:
                        print("c d s 2")
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1
                elif culdesac == 1:
                    print(map_droite)
                    FENETRE.blit(game_over, (0, 0))
                    print("blblb")
                    map_haut = 0
                    map_droite = 0
                    map_gauche = 0
                    print(niveau1)
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            niveau2 = False
                            i=0
                        
                else :
                    if map_haut != 0:
                        i += 1
                        map_haut = 0
                        map_droite = 0
                        map_gauche = 0 
                            
                if i == 7 :
                    FENETRE.blit(FINISH, (0,0))
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            niveau2 = False
                            map_gauche = 0
                            map_droite = 0
                            map_haut = 0
                            map_bas = 0
                            culdesac = 0
                            map_2.clear()
                            print(map_2)
                            for i in range(7):
                                map_2.append(random.choice([1, 2]))
                            i = 0
                
                elif i > 7 :
                    FENETRE.blit(FINISH, (0,0))
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            niveau2 = False
                            map_gauche = 0
                            map_droite = 0
                            map_haut = 0
                            map_bas = 0
                            culdesac = 0
                            map_2.clear()
                            print(map_2)
                            for i in range(7):
                                map_2.append(random.choice([1, 2]))
                            i = 0
                            
                keys_pressed = pygame.key.get_pressed() 
                perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                FENETRE.blit(PERSO, (perso.x, perso.y))
                                
            elif niveau3:
                #print('niv3')
                pass

            else:
        
        
                FENETRE.blit(FOND2, (0, 0))
                FENETRE.blit(NIVEAU1, (200,230))
                FENETRE.blit(NIVEAU2, (400,250))
                FENETRE.blit(NIVEAU3, (600,260))

        pygame.display.update()  # rafraichissement de la page

    pygame.quit()  # fermeture propre de la fenêtre


if __name__ == "__main__":
    main()

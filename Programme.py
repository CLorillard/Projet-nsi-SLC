#importation des bibliothèques et modules
import pygame, time, os, random
from pygame.locals import *
pygame.init()
pygame.mixer.init()

#ouverture de la fenetre pygame et définition taille de la fenetre
WIDTH, HEIGHT = 1000, 700
FENETRE = pygame.display.set_mode((WIDTH, HEIGHT))
#nom de la fenetre
pygame.display.set_caption("CANDY MAZE")

#Chargement des fonds
FOND_1 = pygame.image.load("image/background.jpg").convert()
FOND = pygame.transform.scale(FOND_1, (WIDTH, HEIGHT))

game_over_1= pygame.image.load("image/gameover.jpg").convert()
game_over = pygame.transform.scale(game_over_1, (WIDTH, HEIGHT))

cul_de_sac_1= pygame.image.load("image/culdesac.jpg").convert()
cul_de_sac_2=pygame.transform.rotate(cul_de_sac_1,+90)
cul_de_sac = pygame.transform.scale(cul_de_sac_2, (WIDTH, HEIGHT))

FOND2_1=pygame.image.load("image/FOND2.jpg").convert()
FOND2 = pygame.transform.scale(FOND2_1, (WIDTH, HEIGHT))

FINISH_1=pygame.image.load("image/maison.jpg").convert()#Map de fin
FINISH= pygame.transform.scale(FINISH_1, (WIDTH, HEIGHT))

che2_1=pygame.image.load("image/deuxchemin.jpg").convert()#Map du chemin a deux issus
che2_2= pygame.transform.rotate(che2_1,90)
che2 = pygame.transform.scale(che2_2, (WIDTH, HEIGHT))

che3_1=pygame.image.load("image/troischemins.jpg").convert()#Map du chemin a trois issus
che3_2= pygame.transform.rotate(che3_1,90)
che3 = pygame.transform.scale(che3_2, (WIDTH, HEIGHT))

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

NOTICE_1 = pygame.image.load("image/regles.png").convert() #importation de l'image NOTICE
NOTICE =  pygame.transform.scale(NOTICE_1, (700,300))

NIVEAU_1 = pygame.image.load("image/niveau1.png").convert_alpha() #importation de l'image niveau1
NIVEAU1 =  pygame.transform.scale(NIVEAU_1, (200,350))

NIVEAU_2 = pygame.image.load("image/niveau2.png").convert_alpha() #importation de l'image niveau2
NIVEAU2 =  pygame.transform.scale(NIVEAU_2, (200,350))

NIVEAU_3 = pygame.image.load("image/niveau3.png").convert_alpha() #importation de l'image niveau3
NIVEAU3 =  pygame.transform.scale(NIVEAU_3, (200,350))

TIME_1 = pygame.image.load("image/clock_icon.png").convert_alpha() #importation de l'image chronometre
TIME =  pygame.transform.scale(TIME_1, (20,20))

TIMEWIN_1 = pygame.image.load("image/trophy_icon.png").convert_alpha() #importation de l'image pour le meilleur temps
TIMEWIN =  pygame.transform.scale(TIMEWIN_1, (50,50))


#variables couleurs
WHITE = (255, 255, 255)
color_light = (130,170,210)
color_dark = (100,125,190)
ROSE = (211,50,100)

#police et taille de texte
bigfont = pygame.font.SysFont('arial',35)
smallfont=pygame.font.SysFont('arial',25)

#Texte
text = bigfont.render('?' , True , WHITE)
score=smallfont.render('TEMPS:' , True , WHITE)
score2=smallfont.render('MEILLEUR TEMPS:' , True , WHITE)

#Liste des indices necessaires pour gagner selon les niveaux(1/2/3)
map_1 = []
for i in range(7):
    map_1.append(random.choice([1, 2]))

map_2 = []
for i in range(13):
    map_2.append(random.choice([1,2]))

map_3 = []
for i in range(12):
    map_3.append(random.choice([1,2,3]))

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

#fonction principale
def main():
    perso = pygame.Rect(450, 600, PERSO_WIDTH, PERSO_HEIGHT) #coordonnées du perso avec la fonction rect
    clock = pygame.time.Clock()
    #pygame.mixer.music.play(-1,0.0)
    tZero=time.time() #Récupération de tZero
    #initialisation des variables/listes/booléens
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
    map_milieu = 0
    culdesac = 0
    i=0
    game_over_45 = 0
    choix = []
    choix.append(random.choice([1,2]))

    while run:

        FENETRE.blit(FOND, (0,0)) #affichage du fond
        for event in pygame.event.get(): #pour les actions effectués dans la fenetre pygame
            if event.type == pygame.QUIT:    #si on ferme la fenetre
                run = False    # alors run = 0 donc sort de la boucle while

            if event.type == pygame.MOUSEBUTTONDOWN: #si on appuie sur la souris
                if WIDTH-30 <= mouse[0] <= WIDTH-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40: #position de la souris sur l'ecran
                    if aide== False:#si l'aide n'est pas ouverte
                        aide=True #ouvre l'aide
                    else:
                        aide=False#n'ouvre pas l'aide ou la ferme
                #bouton niveau 1
                if WIDTH-825 <= mouse[0] <= WIDTH-825+175 and HEIGHT-450 <= mouse[1] <= HEIGHT-450+300 and jouer:
                    if niveau1==False:
                        niveau1=True

                #bouton niveau 2
                if WIDTH-600 <= mouse[0] <= WIDTH-600+175 and HEIGHT-450 <= mouse[1] <= HEIGHT-450+300 and jouer:
                    if niveau2==False:
                        niveau2=True

                #bouton niveau 3
                if WIDTH-375 <= mouse[0] <= WIDTH-425+175 and HEIGHT-450 <= mouse[1] <= HEIGHT-450+300 and jouer:
                    if niveau3==False:
                        niveau3=True

                #bouton jouer
                if WIDTH-750 <= mouse[0] <= WIDTH-750+500 and HEIGHT-400 <= mouse[1] <= HEIGHT-400+200:
                    if jouer==False:
                        jouer=True

        mouse = pygame.mouse.get_pos() #coordonnées de la souris
        if WIDTH-30 <= mouse[0] <= WIDTH-30+40 and HEIGHT-690 <= mouse[1] <= HEIGHT-690+40:
            pygame.draw.rect(FOND,color_light,[WIDTH-40,HEIGHT-690,40,40]) #crée un rectangle gris clair si on passe la souris dessus
            FENETRE.blit(text , (WIDTH-30,HEIGHT-690))

        else:
            pygame.draw.rect(FOND,color_dark,[WIDTH-40,HEIGHT-690,40,40]) #crée un rectangle gris foncé si la souris n'est pas dessus
            FENETRE.blit(text , (WIDTH-30,HEIGHT-690))#affiche le point d'interrogation sur le rectangle


        if aide:
            FENETRE.blit(NOTICE,(50,0))#affichage de l'image aide


        if jouer:#si on a appuyé sur "jouer"

            if niveau1:#si on a choisis le niveau 1

                print(map_1)

                FENETRE.blit(droit, (0, 0))#affichage de la map de depart
                if perso.y - DIST <= 0:
                    if WIDTH-940 <= perso.x <= WIDTH-940+355 and map_haut:
                        map_gauche+=1

                    elif WIDTH-410 <= perso.x <= WIDTH-410+345 and map_haut:
                        map_droite+=1
                    map_haut+=1
                    perso.y = perso.y + 700

                if map_haut ==1:
                    FENETRE.blit(che2, (0, 0))
                    chemin_2 = 1

                elif map_haut ==2:
                    if map_gauche == 1 and map_1[i]==1:
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1

                    elif map_gauche == 1 and map_1[i]==2:
                        FENETRE.blit(toutdroit, (0, 0))

                    elif map_droite == 1 and map_1[i]==1:
                        FENETRE.blit(toutdroit2, (0,0))

                    elif map_droite == 1 and map_1[i]==2:
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1

                elif culdesac == 1:

                    FENETRE.blit(game_over, (0, 0))#affichage de l'image Game over
                    FENETRE.blit(TIMEWIN,(WIDTH-700,HEIGHT-500))#affichage de l'image pour le meilleur temps
                    FENETRE.blit(TIME,(WIDTH-685,HEIGHT-525))#affichage de l'image horloge
                    FENETRE.blit(score , (WIDTH-630,HEIGHT-525))#texte temps
                    FENETRE.blit(score2 , (WIDTH-630,HEIGHT-480))#texte meilleur temps
                    game_over_45 = 1 #la variable passe à 1
                    i=0 #i revient a 0

                    #si on appuie sur "rejouer" les variables retournent à 0

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
                                tZero=time.time() #Récupération de tZero

                        elif event.type == pygame.KEYDOWN:#si on appuie sur "Entrée" les variables retournent à 0 et on arrive sur l'écran principal car niveau 1 devient false
                            if event.key == K_RETURN:
                                niveau1 = False
                                game_over_45 = 0
                                map_gauche = 0
                                map_droite = 0
                                map_haut = 0
                                map_bas = 0
                                culdesac = 0
                                i = 0
                                tZero=time.time()


                else :
                    if map_haut != 0:
                        i += 1
                        map_haut = 0
                        map_droite = 0
                        map_gauche = 0


                if i >= 7 :
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
                            for i in range(7):
                                map_1.append(random.choice([1, 2]))
                            i = 0

                if game_over_45 != 1:
                    keys_pressed = pygame.key.get_pressed()
                    perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                    FENETRE.blit(PERSO, (perso.x, perso.y))
                    Start_time=time.time()#temps depart
                    Actual_time=Start_time-tZero
                    texts = smallfont.render(str(round(Actual_time)), True, (255,255,255))#transformation du temps en texte
                    pygame.draw.rect(FENETRE,ROSE,[WIDTH-999,HEIGHT-690,62,30])#creation zone pour affichage temps
                    FENETRE.blit(texts,(20,10))#affichage du temps
                    FENETRE.blit(TIME, (0,15))#affichage icon horloge

            elif niveau2:

                print(map_2)
                FENETRE.blit(droit, (0, 0))
                if perso.y - DIST <= 0:
                    if WIDTH-940 <= perso.x <= WIDTH-940+355 and map_haut:
                        map_gauche+=1

                    elif WIDTH-410 <= perso.x <= WIDTH-410+345 and map_haut:
                        map_droite+=1
                    map_haut+=1
                    perso.y = perso.y + 700

                if map_haut ==1:
                    FENETRE.blit(che2, (0, 0))
                    chemin_2 = 1

                elif map_haut ==2:
                    if map_gauche == 1 and map_1[i]==1:
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1

                    elif map_gauche == 1 and map_1[i]==2:
                        FENETRE.blit(toutdroit, (0, 0))

                    elif map_droite == 1 and map_1[i]==1:
                        FENETRE.blit(toutdroit2, (0,0))

                    elif map_droite == 1 and map_1[i]==2:
                        FENETRE.blit(cul_de_sac, (0,0))
                        culdesac = 1

                elif culdesac == 1:
                    print(map_droite)
                    FENETRE.blit(game_over, (0, 0))
                    FENETRE.blit(TIMEWIN,(WIDTH-700,HEIGHT-500))
                    FENETRE.blit(TIME,(WIDTH-685,HEIGHT-525))
                    FENETRE.blit(score , (WIDTH-630,HEIGHT-525))
                    FENETRE.blit(score2 , (WIDTH-630,HEIGHT-480))
                    game_over_45 = 1
                    i=0

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
                                tZero=time.time()

                        elif event.type == pygame.KEYDOWN:
                            if event.key == K_RETURN:
                                niveau2 = False
                                game_over_45 = 0
                                map_gauche = 0
                                map_droite = 0
                                map_haut = 0
                                map_bas = 0
                                culdesac = 0
                                i = 0
                                tZero=time.time()

                elif game_over_45 == 1 :
                    FENETRE.blit(game_over, (0, 0))

                else :
                    if map_haut != 0:
                        i += 1
                        map_haut = 0
                        map_droite = 0
                        map_gauche = 0


                if i >= 13 :
                    FENETRE.blit(FINISH, (0,0))
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            niveau2 = False
                            i = 0
                            print(i)
                            map_gauche = 0
                            map_droite = 0
                            map_haut = 0
                            map_bas = 0
                            culdesac = 0
                            tZero=time.time()
                            map_2.clear()
                            print(map_2)
                            for i in range(13):
                                map_2.append(random.choice([1, 2]))
                            i = 0

                if game_over_45 != 1:
                    keys_pressed = pygame.key.get_pressed()
                    perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                    FENETRE.blit(PERSO, (perso.x, perso.y))
                    Start_time=time.time()#temps depart
                    Actual_time=Start_time-tZero
                    texts = smallfont.render(str(round(Actual_time)), True, (255,255,255))#transformation du temps en texte
                    pygame.draw.rect(FENETRE,ROSE,[WIDTH-999,HEIGHT-690,62,30])#creation zone pour affichage temps
                    FENETRE.blit(texts,(20,10))#affichage du temps
                    FENETRE.blit(TIME, (0,15))#affichage icon horloge

            elif niveau3:

                print(map_3)

                FENETRE.blit(droit, (0, 0))

                if choix[0] == 1 and map_3[i] != 3:
                    FENETRE.blit(droit, (0, 0))
                    if perso.y - DIST <= 0:
                        if WIDTH-940 <= perso.x <= WIDTH-940+355 and map_haut:
                            map_gauche+=1

                        elif WIDTH-410 <= perso.x <= WIDTH-410+345 and map_haut:
                            map_droite+=1
                        map_haut+=1
                        perso.y = perso.y + 700

                    if map_haut ==1:
                        FENETRE.blit(che2, (0, 0))
                        chemin_2 = 1

                    elif map_haut ==2:
                        if map_gauche == 1 and map_1[i]==1:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                        elif map_gauche == 1 and map_1[i]==2:
                            FENETRE.blit(toutdroit, (0, 0))

                        elif map_droite == 1 and map_1[i]==1:
                            FENETRE.blit(toutdroit2, (0,0))

                        elif map_droite == 1 and map_1[i]==2:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                    elif culdesac == 1:
                        FENETRE.blit(game_over, (0, 0))
                        FENETRE.blit(TIMEWIN,(WIDTH-700,HEIGHT-500))
                        FENETRE.blit(TIME,(WIDTH-685,HEIGHT-525))
                        FENETRE.blit(score , (WIDTH-630,HEIGHT-525))
                        FENETRE.blit(score2 , (WIDTH-630,HEIGHT-480))
                        game_over_45 = 1
                        i=0

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
                                    tZero=time.time()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == K_RETURN:
                                    niveau3 = False
                                    game_over_45 = 0
                                    map_gauche = 0
                                    map_droite = 0
                                    map_haut = 0
                                    map_bas = 0
                                    culdesac = 0
                                    i = 0
                                    tZero=time.time()

                    elif game_over_45 == 1 :
                        FENETRE.blit(game_over, (0, 0))

                    else :
                        if map_haut != 0:
                            i += 1
                            map_haut = 0
                            map_droite = 0
                            map_gauche = 0

                else :
                    FENETRE.blit(droit, (0, 0))
                    if perso.y - DIST <= 0:
                        if WIDTH-976 <= perso.x <= WIDTH-976+272 and map_haut:
                            map_gauche+=1

                        elif WIDTH-654 <= perso.x <= WIDTH-654+321 and map_haut:
                            map_milieu+=1

                        elif WIDTH-284 <= perso.x <= WIDTH-284+282 and map_haut:
                            map_droite+=1

                        map_haut+=1
                        perso.y = perso.y + 700

                    if map_haut ==1:
                        FENETRE.blit(che3, (0, 0))

                    elif map_haut ==2:
                        if map_gauche == 1 and map_3[i]==1:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                        elif map_gauche == 1 and map_3[i]==2:
                            FENETRE.blit(toutdroit, (0, 0))
                            choix.clear()
                            choix.append(random.choice([1,2]))

                        elif map_gauche == 1 and map_3[i]==3:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                        elif map_milieu == 1 and map_3[i]==1:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                        elif map_milieu == 1 and map_3[i]==2:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                        elif map_milieu == 1 and map_3[i]==3:
                            FENETRE.blit(droit, (0, 0))
                            choix.clear()
                            choix.append(random.choice([1,2]))

                        elif map_droite == 1 and map_3[i]==1:
                            FENETRE.blit(toutdroit2, (0,0))
                            choix.clear()
                            choix.append(random.choice([1,2]))

                        elif map_droite == 1 and map_3[i]==2:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                        elif map_droite == 1 and map_3[i]==3:
                            FENETRE.blit(cul_de_sac, (0,0))
                            culdesac = 1

                    elif culdesac == 1:
                        print(map_droite)
                        FENETRE.blit(game_over, (0, 0))
                        FENETRE.blit(TIMEWIN,(WIDTH-700,HEIGHT-500))
                        FENETRE.blit(TIME,(WIDTH-685,HEIGHT-525))
                        FENETRE.blit(score , (WIDTH-630,HEIGHT-525))
                        FENETRE.blit(score2 , (WIDTH-630,HEIGHT-480))
                        game_over_45 = 1
                        i=0

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
                                    tZero=time.time()

                            elif event.type == pygame.KEYDOWN:
                                if event.key == K_RETURN:
                                    niveau3 = False
                                    game_over_45 = 0
                                    map_gauche = 0
                                    map_droite = 0
                                    map_haut = 0
                                    map_bas = 0
                                    culdesac = 0
                                    i = 0
                                    tZero=time.time()

                    elif game_over_45 == 1 :
                        FENETRE.blit(game_over, (0, 0))

                    else :
                        if map_haut != 0:
                            i += 1
                            map_haut = 0
                            map_droite = 0
                            map_gauche = 0


                if i >= 12 :
                    FENETRE.blit(FINISH, (0,0))
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            niveau3 = False
                            i = 0
                            print(i)
                            map_gauche = 0
                            map_droite = 0
                            map_haut = 0
                            map_bas = 0
                            culdesac = 0
                            tZero=time.time()
                            map_3.clear()
                            print(map_1)
                            for i in range(12):
                                map_3.append(random.choice([1, 2, 3]))
                            i = 0

                if game_over_45 != 1:
                    keys_pressed = pygame.key.get_pressed()
                    perso_mouvement(keys_pressed,perso)  #appel fonction mouvement perso
                    FENETRE.blit(PERSO, (perso.x, perso.y))
                    Start_time=time.time()#temps depart
                    Actual_time=Start_time-tZero
                    texts = smallfont.render(str(round(Actual_time)), True, (255,255,255))#transformation du temps en texte
                    pygame.draw.rect(FENETRE,ROSE,[WIDTH-999,HEIGHT-690,62,30])#creation zone pour affichage temps
                    FENETRE.blit(texts,(20,10))#affichage du temps
                    FENETRE.blit(TIME, (0,15))#affichage icon horloge

            else:
                FENETRE.blit(FOND2, (0, 0))#map du menu
                FENETRE.blit(NIVEAU1, (200,230))#icone niveau 1
                FENETRE.blit(NIVEAU2, (400,250))#icone niveau 2
                FENETRE.blit(NIVEAU3, (600,260))#icone niveau 3

        pygame.display.update()  # rafraichissement de la page

    pygame.quit()  # fermeture propre de la fenêtre

if __name__ == "__main__":
    main() #appel fonction principale

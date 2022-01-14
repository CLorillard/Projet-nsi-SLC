import pygame
from pygame.locals import *
pygame.init()
  
# screen resolution
res = (640,480)
  
# opens up a window
screen = pygame.display.set_mode(res)
fond= pygame.image.load("image/background.jpg").convert()
screen.blit(fond, (0,0))


#importation de l'image notice
notice=pygame.image.load("image/regles.png").convert()
#creation des variables pour la couleur du bouton
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
#c
largeur = screen.get_width()
hauteur = screen.get_height()
  

smallfont = pygame.font.SysFont('arial',35)
text = smallfont.render('?' , True , color)
aide= False
running=True

while running:
    screen.blit(fond, (0,0)) 
    if aide:
        screen.blit(notice,(50,0))
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if largeur-20 <= mouse[0] <= largeur-20+40 and hauteur-470 <= mouse[1] <= hauteur-470+40:
                if aide== False:
                    aide=True
                else:
                    aide=False
                
    mouse = pygame.mouse.get_pos()
    if largeur-20 <= mouse[0] <= largeur-20+40 and hauteur-470 <= mouse[1] <= hauteur-470+40:
        pygame.draw.rect(screen,color_light,[largeur-20,hauteur-470,40,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[largeur-20,hauteur-470,40,40])
    screen.blit(text , (largeur-20,hauteur-470))
      
    pygame.display.update()
pygame.quit()

import pygame
from pygame.locals import *

# initializing the constructor
pygame.init()
  
# screen resolution
res = (640,480)
  
# opens up a window
screen = pygame.display.set_mode(res)
fond= pygame.image.load("images/background.jpg").convert()
screen.blit(fond, (0,0))



notice=pygame.image.load("images/regles.png").convert()
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
largeur = screen.get_width()
hauteur = screen.get_height()
  

smallfont = pygame.font.SysFont('arial',35)
text = smallfont.render('?' , True , color)
  
while True:
      
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if largeur/2 <= mouse[0] <= largeur/2+40 and hauteur/2 <= mouse[1] <= hauteur/2+40:
                fenetre = pygame.display.set_mode((1271, 457))
                fenetre.blit(notice,(0,0))
                
    mouse = pygame.mouse.get_pos()
    if largeur/2 <= mouse[0] <= largeur/2+40 and hauteur/2 <= mouse[1] <= hauteur/2+40:
        pygame.draw.rect(screen,color_light,[largeur/2,hauteur/2,40,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[largeur/2,hauteur/2,40,40])
    screen.blit(text , (largeur/2,hauteur/2))
      
    pygame.display.update()

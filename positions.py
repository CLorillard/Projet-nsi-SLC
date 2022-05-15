def perso_mouvement(keys_pressed,perso):

    if DANGER == 1:
        if keys_pressed[pygame.K_LEFT] and perso.x > 321:
            perso.x -= DIST  #perso se déplace à gauche
        if keys_pressed[pygame.K_RIGHT]and perso.x < 669:
            perso.x += DIST   #perso se déplace  à droite
        if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:
            perso.y -= DIST    #perso se déplace vers le haut
        if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:
            perso.y += DIST    #perso se déplace vers le bas

    if DROIT_D == 1:
        if perso.y < 360:
            if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and perso.x > 321:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT]and perso.x + 100 < 669:
                perso.x += DIST
        else :
            if keys_pressed[pygame.K_UP] and perso.y + 140 > 0.97*perso.x :
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and perso.y  < 0.97*perso.x :
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and perso.x*0.97 > perso.y:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT] and perso.x*0.97  < perso.y + 140:
                perso.x += DIST

    if DROIT_G == 1:
        if perso.y < 360:
            if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and perso.x > 321:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT]and perso.x + 100 < 669:
                perso.x += DIST
        else :
            if keys_pressed[pygame.K_UP] and perso.y+ 100  > -0.765*(perso.x-950):
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and perso.y -60 < -0.755*(perso.x-950) :
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and -0.765*(perso.x-950) < perso.y + 100:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT]and -0.755*(perso.x-950) > perso.y -60 :
                perso.x += DIST

    if CHEMINS_2 == 1:
        if perso.y > 360 :
            if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and perso.x > 321:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT]and perso.x + 100 < 669:
                perso.x += DIST

        elif perso.y < 120 :
            if perso.x > 505 :

                if keys_pressed[pygame.K_UP] and (perso.x + 450-1000)*(-1.55) < perso.y :
                    perso.y -= DIST
                if keys_pressed[pygame.K_DOWN] and 1.33*(perso.x +60) > perso.y + 180 and -1.47*(perso.x-1000) > perso.y + 300 :
                    perso.y += DIST
                if keys_pressed[pygame.K_LEFT] and (perso.x + 450-1000)*(-1.55) < perso.y:
                    perso.x -= DIST
                if keys_pressed[pygame.K_RIGHT] and -1.47*(perso.x-1000) > perso.y + 300  :
                    perso.x += DIST
            else:
                if keys_pressed[pygame.K_UP] and (perso.x-250 )*1.33 < perso.y+150:
                    perso.y -= DIST
                if keys_pressed[pygame.K_DOWN] and 1.33*(perso.x +60) > perso.y + 180 and -1.47*(perso.x-1000) > perso.y + 300 :
                    perso.y += DIST
                if keys_pressed[pygame.K_LEFT] and 1.33*(perso.x +60) > perso.y + 180:
                    perso.x -= DIST
                if keys_pressed[pygame.K_RIGHT] and (perso.x-250 )*1.33 < perso.y+150:
                    perso.x += DIST
        else :
            if keys_pressed[pygame.K_UP]  :
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and 1.33*(perso.x +60) > perso.y + 180 and -1.47*(perso.x-1000) > perso.y + 300 :
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and 1.33*(perso.x +60) > perso.y + 180:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT] and -1.47*(perso.x-1000) > perso.y + 300  :
                perso.x += DIST

    if CHEMINS_3 == 1:
        if perso.y > 360 :
            if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and perso.x > 321:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT]and perso.x + 100 < 669:
                perso.x += DIST

        else :
            if keys_pressed[pygame.K_UP]  :
                perso.y -= DIST
            if keys_pressed[pygame.K_DOWN] and 1.5*(perso.x -24) > perso.y +50 and -1.7*(perso.x-1000) > perso.y + 300 :
                perso.y += DIST
            if keys_pressed[pygame.K_LEFT] and 1.5*(perso.x -24) > perso.y + 50:
                perso.x -= DIST
            if keys_pressed[pygame.K_RIGHT] and -1.7*(perso.x-1000) > perso.y + 300 :
                perso.x += DIST

    if GAGNER == 1:
        if keys_pressed[pygame.K_UP] and perso.y - DIST > 300:
            perso.y -= DIST
        if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:
            perso.y += DIST
        if keys_pressed[pygame.K_LEFT] and perso.x > 321:
            perso.x -= DIST
        if keys_pressed[pygame.K_RIGHT]and perso.x + 100 < 669:
            perso.x += DIST

    else :
        if keys_pressed[pygame.K_UP] and perso.y - DIST > 0:
            perso.y -= DIST
        if keys_pressed[pygame.K_DOWN] and perso.y + DIST < HEIGHT - PERSO_HEIGHT:
            perso.y += DIST
        if keys_pressed[pygame.K_LEFT] and perso.x > 280:
            perso.x -= DIST
        if keys_pressed[pygame.K_RIGHT]and perso.x  < 665:
            perso.x += DIST
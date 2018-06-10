import pygame
import time
from random import*
#On annonce les bibliothèques dont nous auront besoin

blue = (7,3,54) 
white = (255,255,255)
#Ici, les couleurs de fond de de typo (police d'écritures) sont données.
pygame.mixer.init()
pygame.init()
#On initalise les biblios'

BordLargeur = 800
BordHauteur = 500
ShipLargeur = 50
ShipHauteur = 66
MursLargeur = 300
MursHauteur = 300
#On nomme des variables, et ont leurs attribue des valeurs

fenetre = pygame.display.set_mode((BordLargeur,BordHauteur))
pygame.display.set_caption("Striker Challenge !")
#On donne des infos sur la page (Dimension en fonction de BordLargeur et Hauteur (Variables) et le nom de la page)
clock = pygame.time.Clock()
#On lance une horloge virtuelle pour mettre en "pause" le jeu pendant les "GameOver" ,
#on met le processus en "Standby" jusqu'à un input


img = pygame.image.load('Ship.png')
MursSprite1 = pygame.image.load('Wall2haut.png')
MursSprite2 = pygame.image.load('Wall2Bas.png')
#On annonce que deux images seront "loadés" "Chargés"

##########################################################
# La partie contenant des DEF traduit une création d' "Objets",
# C'est à dire, on ajoute un item, en codant ses interaction, ses réactions, positions.

def score(compte) :
    police = pygame.font.Font('prstartk.ttf', 16)
    texte = police.render("Score : " + str(compte), True, white)
    fenetre.blit(texte, [10,0])
#Ici, on choisi la Typo et la position d'affichage du score
def murs(x_murs, y_murs, espace):
    fenetre.blit(MursSprite1, (x_murs, y_murs))
    fenetre.blit(MursSprite2,(x_murs,y_murs+ MursHauteur +espace))


def Replay():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type ==pygame.KEYUP:
            continue
        return event.key
    return  None
 #Ici, on gère le "Rejouer" en cas d'input, le jeu se relance,
 #sinon, en fermant le jeu, on ferme le jeu (Quit permet d'éviter un crash"


def creaTexteObjs (texte, font):
    textefenetre = font.render(texte,True,white)
    return textefenetre, textefenetre.get_rect()
#Blanc pour la couleur du Texte

def msgfenetre (texte):
    GOTexte = pygame.font.Font('Pixel.otf', 150)
    petitTexte = pygame.font.Font('prstartk.ttf',20)

    titreTexteSurf, titreTexteRect = creaTexteObjs(texte, GOTexte)
    titreTexteRect.center = BordLargeur/2,((BordHauteur/2)-50)
    fenetre.blit(titreTexteSurf, titreTexteRect)

    petitTexteSurf, petitTexteRect = creaTexteObjs\
        ("Reesayer ?", petitTexte )
    petitTexteRect.center = BordLargeur/2, ((BordHauteur/2) +50)
    fenetre.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()
    time.sleep(2)

    while Replay() == None :
        clock.tick()

    main()
#Message de Game Over, avec les positions précise d'affichage et la taille du texte
def gameOver():
    msgfenetre("Perdu!")

def Ship(x,y, image):
    fenetre.blit(image, (x,y))

def main():
    x=150
    y=200
    y_move=0

    x_murs = BordLargeur
    y_murs = randint(-300,10)
    espace = ShipHauteur*3
    VitesseDesMurs = 3
#C'est les murs qui avancent , pas nous !
    Score_debut = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound("explode.ogg").play()
                while pygame.mixer.get_busy():
                    # lecture en cours
                    pass
                game_over= True
                #Ici, on dit que si il y a collision entre un objet et le Ship, un son se lance, affichant ensuite l'écran de GameOver

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_move = 3
            if event.type ==pygame.KEYUP :
                y_move = 0

        y += y_move

        fenetre.fill(blue)
        Ship(x,y,img)

        murs(x_murs,y_murs, espace)

        score(Score_debut)

        x_murs -=VitesseDesMurs


        if y>BordHauteur -40 or y <-10:
            gameOver()

        if x_murs < (-1*MursLargeur):
            x_murs = BordLargeur
            y_murs = randint(-300,10)

            if 3 <= Score_debut < 5:
                VitesseDesMurs = 7
                espace = ShipHauteur*2.8
            if 5 <= Score_debut < 7 :
                VitesseDesMurs = 8
                espace = ShipHauteur*2.7
            if 7 <= Score_debut < 10 :
                VitesseDesMurs = 9
                espace = ShipHauteur*2.5
            if 10 <= Score_debut <22:
                VitesseDesMurs = 11
                espace = ShipHauteur*2.2
            if 22 <= Score_debut:
                VitesseDesMurs = 13
                espace = ShipHauteur*2
#Ici, on trouve la difficulté croissante, pour un certain nombre de portes passés, la vitesses des murs augmente


        if x +ShipLargeur > x_murs + 40 :
            if y < y_murs + MursHauteur  -50:
                if x - ShipLargeur < x_murs +MursLargeur -20 :
                    #print("touche haut!!!")
                    pygame.mixer.Sound("explode.ogg").play()
                    while pygame.mixer.get_busy():
                        # lecture en cours
                        pass
                    gameOver()

        if x +ShipLargeur >x_murs + 40 :
            if y +ShipHauteur > y_murs + MursHauteur + espace +50 :
                if x -ShipLargeur < x_murs+ MursLargeur - 20:
                    #print("touche bas!!!")
                    pygame.mixer.Sound("explode.ogg").play()
                    while pygame.mixer.get_busy():
                        # lecture en cours
                        pass
                    gameOver()

        if x_murs < (x-MursLargeur)<x_murs+VitesseDesMurs :
            Score_debut +=1
            #Ici, a chaque porte passée, on fait +1 au score
           
        pygame.display.update()

#Ici, on rafraichit l'affichage , pour éviter les bug, et avoir des déplacement fluides (Voilà pourquoi on le mets a la fin du programme)

main()
pygame.quit()
quit()

import pygame
from random import randint
from grand_petit import grand_petit
from main_tusmo import tusmo
from qui_est_ce import qui_est_ce

class Joueur:
    def __init__(self,identifiant):
        self.id = identifiant
        self.score = 0

joueur = Joueur(0)
joueur1 = Joueur(1)
joueur2 = Joueur(2)

pygame.init()

largeur = pygame.display.Info().current_w
hauteur = pygame.display.Info().current_h
ecran = pygame.display.set_mode([largeur,hauteur-60]) # (largeur,hauteur)
pygame.display.set_caption("OJC Games")

ecran.fill((255, 255, 255))

def bouton(ecran,centre,couleur,w,h):
    """Dessiner un bouton

    Paramètres
    ----------
    ecran : la fenêtre de jeu sur laquelle sera dessiné le bouton
    centre : tuple (x,y)
        coordonnées du centre du bouton
    couleur : tuple (r,g,b)
        la couleur en RGB du bouton
    w : int
        la largeur de la surface
    h : int
        la hauteur de la surface

    Retourne
    --------
    bouton : rect
        le bouton
    """
    surface = pygame.Surface((w,h))
    surface.fill(couleur)
    bouton = surface.get_rect()
    bouton.center= centre
    ecran.blit(surface,bouton)
    return bouton

def texte_bouton(ecran,bouton,texte,taille,couleur):
    """Ajouter du texte sur un bouton

    Paramètres
    ----------
    ecran : la fenêtre
    bouton : rect
        un bouton (créé avec la fonction bouton
    texte : str
        le texte à ajouter sur le bouton
    taille : int
        la taille de la police
    couleur : tuple (r,g,b)
        la couleur de la police

    Retourne
    --------
    bouton = le bouton avec le texte
    """
    police = pygame.font.Font(None,taille)
    surface = police.render(texte,True,couleur)
    txt = surface.get_rect(center=bouton.center)
    ecran.blit(surface,txt)
    return bouton  

def titre(ecran,centre,texte,taille,couleur):
    """Ajouter un texte à l'écran

    Paramètres
    ----------
    ecran : l'écran où va s'afficher le texte
    centre : tuple (x,y)
        les coordonnées du centre du texte
    texte : str
        le texte à afficher
    taille : int
        la taille dela police
    couleur : tuple (r,g,b)
        la couleur du texte
    """
    police = pygame.font.Font(None,taille)
    surface = police.render(texte,True,couleur)
    rect = surface.get_rect()
    rect.center = centre
    ecran.blit(surface,rect)

def accueil(ecran,largeur,hauteur):
    centre = (largeur//2,hauteur//2)
    bleu = (204,229,255)
    rect = bouton(ecran,centre,bleu,400,250)
    rect = texte_bouton(ecran,rect,"JOUER",80,(0,0,0))
    noir = (0,0,0)
    haut = (largeur//2,hauteur//5)
    bienvenue = titre(ecran,haut,"Bienvenue sur la plateforme de jeu OCJ Games !",50,noir)
    pygame.display.flip()
    # attention ne pas oublier ça sinon ça n'affiche rien !
    return rect

def joueurs(ecran,largeur,hauteur):
    # Couleur de fond
    ecran.fill((204,229,255))
    # Positions
    centre_gauche = (largeur//4,hauteur//2)
    centre_droit = (largeur*3//4,hauteur//2)
    haut = (largeur//2,hauteur//5)
    # Couleurs
    blanc = (255,255,255)
    noir = (0,0,0)
    # 1er bouton
    joueur1 = bouton(ecran,centre_gauche,blanc,200,150)
    joueur1 = texte_bouton(ecran,joueur1,"1 joueur",40,noir)
    # Texte
    nb_joueur = titre(ecran,haut,"Combien de joueurs ?",50,noir)
    # 2e bouton
    joueur2 = bouton(ecran,centre_droit,blanc,200,150)
    joueur2 = texte_bouton(ecran,joueur2,"2 joueurs",40,noir)
    
    pygame.display.flip()
    return (joueur1,joueur2)
    
def parties(ecran,largeur,hauteur):
    ecran.fill((255,255,255))
    haut = (largeur//2,hauteur//5)
    centre_haut = (largeur//2,hauteur//3+50)
    noir = (0,0,0)
    bleu = (204,229,255)
    nb_parties = titre(ecran,haut,"Combien de parties voulez-vous faire ?",50,noir)
    titre(ecran,centre_haut,"Entrez le nombre puis appuyez sur la touche Entrer",40,noir)
    pygame.display.flip()
    """
    boutons = []
    for i in range(1,11):
        w = 100
        rect = bouton(ecran,(w+i*100,hauteur//2),bleu,75,75)
        rect = texte_bouton(ecran,rect,str(i),40,noir)
        boutons.append(rect)
    return boutons
    """

rect_acc = accueil(ecran,largeur,hauteur)
running = True
home = True
rounds = False
go = False
list_nb = []
nb_parties = ""
while running:
    
    if go :
        print("Nous proposons plusieurs jeux.")
        for i in range(nb_parties):
            if nb_joueurs == 1:
                print("1 : Tusmo, 2 : Plus grand plus petit")
                jeu = int(input("A quel jeu souhaitez-vous jouer ? "))

                if jeu == 1 :
                    if tusmo():
                        joueur.score += 1
                elif jeu == 2 :
                    if grand_petit():
                        joueur.score += 1
                
            else :   # 2 joueurs
                print("1 : Tusmo, 2 : Plus grand plus petit, 3 : Qui-est-ce ?")
                jeu = int(input("A quel jeu souhaitez-vous jouer ? "))
    
                if jeu == 1 :
                    print("C'est au tour du Joueur 1")
                    tusmo1 = tusmo()
                    if tusmo1:
                        joueur1.score += 1
                    print("C'est au tour du Joueur 2")
                    tusmo2 = tusmo()
                    if tusmo2:
                        joueur2.score += 1
                elif jeu == 2 :
                    print("C'est au tour du Joueur 1")
                    if grand_petit():
                        joueur1.score += 1
                    print("C'est au tour du Joueur 2")
                    if grand_petit():
                        joueur2.score += 1
        
                elif jeu == 3 :
                    gagnant = qui_est_ce()
                    if gagnant == 1 :
                        joueur1.score += 1
                    elif gagnant == 2:
                        joueur2.score += 1
                else :
                    print("Entrée invalide.")
            print("Il reste",nb_parties-i-1,"parties")
            
        print("Nombre de parties terminées")
        if nb_joueurs == 1 :
            print("Votre score est de",joueur.score)
        elif nb_joueurs == 2 :
            print("Score du joueur 1 :",joueur1.score)
            print("Score du joueur 2 :",joueur2.score)
            if joueur1.score > joueur2.score :
                print("Le joueur 1 a gagné")
            elif joueur2.score > joueur1.score :
                print("Le joueur 2 a gagné")
            else :
                print("Les deux joueurs sont à ex-aequo")
                running = False
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            # si on touche la petite croix
            pygame.quit()
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # si on appuie sur la touche echap
                pygame.quit()
                running = False
            if rounds :
                cles = [pygame.K_0,pygame.K_1,pygame.K_2,
                        pygame.K_3,pygame.K_4,pygame.K_5,
                        pygame.K_6,pygame.K_7,pygame.K_8,
                        pygame.K_9]
                for i in range(10):
                    if event.key == cles[i]:
                        c = chr(cles[i])
                        list_nb.append(c)
                        
                if event.key == pygame.K_RETURN :
                    for i in range(len(list_nb)):
                        nb_parties = nb_parties + str(list_nb[i])
                    nb_parties = int(nb_parties)
                    print("Vous allez faire",nb_parties,"parties.")
                    rounds = False
                    pygame.quit()
                    go = True
                    
        elif event.type == pygame.MOUSEBUTTONDOWN :
            position = pygame.mouse.get_pos()
            if home :
                if rect_acc.x <= position[0] <= rect_acc.x+rect_acc.width:
                    if rect_acc.y <= position[1] <= rect_acc.y+rect_acc.height:
                        rectangles = joueurs(ecran,largeur,hauteur)
                        rect1 = rectangles[0]
                        rect2 = rectangles[1]
                        home = False
                        players = True
                        
            elif players :
                if rect1.x <= position[0] <= rect1.x + rect1.width:
                    if rect1.y <= position[1] <= rect1.y + rect1.height:
                        nb_joueurs = 1
                        parties(ecran,largeur,hauteur)
                        players = False
                        rounds = True
                        
                elif rect2.x <= position[0] <= rect2.x + rect2.width:
                    if rect2.y <= position[1] <= rect2.y + rect2.height:
                        nb_joueurs = 2
                        parties(ecran,largeur,hauteur)
                        players = False
                        rounds = True
            """
            elif rounds :
                for i in range(10):
                    if boutons[i].x <= position[0] <= boutons[i].x + boutons[i].width:
                        if boutons[i].y <= position[1] <= boutons[i].y + boutons[i].height:
                            nb_parties = i + 1
                            print(nb_parties)
                            go = True
                            rounds = False
                            pygame.quit()
            """           
                        
                
pygame.quit()



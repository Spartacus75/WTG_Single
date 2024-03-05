import pygame
import sys
import time

# Initialiser Pygame
pygame.init()

# Configurer la fenêtre
taille_ecran = largeur, hauteur = 800, 600
ecran = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Simulation de Transport")

# Couleurs
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
BLANC = (255, 255, 255)

# Initialiser le module de police et créer un objet Font
pygame.font.init()
font = pygame.font.SysFont('arial', 20)

# Positions de départ et d'arrivée
point_A = 0
point_B = largeur - 50




# Charger l'image du camion
image_camion_originale = pygame.image.load('images/truck_1.png')
# Supposons que vous voulez redimensionner l'image du camion
nouvelle_largeur = 12  # Nouvelle largeur souhaitée en pixels
nouvelle_hauteur = 3  # Nouvelle hauteur souhaitée en pixels
# Redimensionner l'image du camion
image_camion = pygame.transform.scale(image_camion_originale, (nouvelle_largeur, nouvelle_hauteur))
# Détails du camion
#image_camion = pygame.image.load('images/truck_1.png')
taille_camion = image_camion.get_size()
position_camion = [0, 250]



# Variable pour le suivi du drag
drag_en_cours = False
position_prec = None

# Vitesse de déplacement du camion (pixels par frame)
vitesse = 15

# Direction initiale
direction = "to_B"

# Boucle de jeu
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:  # Bouton gauche enfoncé
            drag_en_cours = True
            position_prec = pygame.mouse.get_pos()
        elif evenement.type == pygame.MOUSEBUTTONUP and evenement.button == 1:  # Bouton gauche relâché
            drag_en_cours = False
        elif evenement.type == pygame.MOUSEMOTION and drag_en_cours:  # Souris déplacée avec bouton gauche enfoncé
            position_actuelle = pygame.mouse.get_pos()
            deplacement_x, deplacement_y = position_actuelle[0] - position_prec[0], position_actuelle[1] - position_prec[1]
            position_camion[0] += deplacement_x
            position_camion[1] += deplacement_y
            position_prec = position_actuelle

    # Effacer l'écran
    ecran.fill(BLANC)
    ecran.blit(image_camion, position_camion)

    # Mettre à jour la position du camion
    if direction == "to_B":
        position_camion[0] += vitesse
        if position_camion[0] >= point_B:
            direction = "stop_B"
    elif direction == "to_A":
        position_camion[0] -= vitesse
        if position_camion[0] <= point_A:
            direction = "stop_A"

    # Gestion des arrêts
    if direction == "stop_B":
        pygame.display.flip()  # Met à jour l'affichage avant de s'arrêter
        time.sleep(1)  # S'arrête pendant 1 seconde
        direction = "to_A"
        image_camion = pygame.transform.flip(image_camion, True, False)
    elif direction == "stop_A":
        pygame.display.flip()  # Met à jour l'affichage avant de s'arrêter
        time.sleep(1)  # S'arrête pendant 1 seconde
        direction = "to_B"
        image_camion = pygame.transform.flip(image_camion, True, False)

    # Afficher la vitesse et les coordonnées du camion
    texte_vitesse = font.render(f'Vitesse: {vitesse} pixels/frame', True, NOIR)
    ecran.blit(texte_vitesse, (10, 10))
    texte_coordonnees = font.render(f'Coordonnées: X={position_camion[0]}, Y={position_camion[1]}', True, NOIR)
    ecran.blit(texte_coordonnees, (10, 35))

    # Actualiser l'affichage
    pygame.display.flip()

    # Limiter les frames par seconde (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

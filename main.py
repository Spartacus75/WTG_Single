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
point_A = 10
point_B = largeur - 50

# Détails du camion
position_camion = [50,250]  # Convertit le tuple en liste pour permettre la modification
taille_camion = (40, 20)

# Vitesse de déplacement du camion (pixels par frame)
vitesse = 10

# Direction initiale
direction = "to_B"

# Boucle de jeu
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

    # Effacer l'écran
    ecran.fill(BLANC)

    # Dessiner le camion
    pygame.draw.rect(ecran, BLEU, (*position_camion, *taille_camion))

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
    elif direction == "stop_A":
        pygame.display.flip()  # Met à jour l'affichage avant de s'arrêter
        time.sleep(1)  # S'arrête pendant 1 seconde
        direction = "to_B"


    # Afficher la vitesse
    texte_vitesse = font.render(f'Vitesse: {vitesse} pixels/frame', True, NOIR)
    ecran.blit(texte_vitesse, (10, 10))


    # Actualiser l'affichage
    pygame.display.flip()

    # Limiter les frames par seconde (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

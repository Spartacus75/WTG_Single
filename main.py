import pygame
import sys
import time
from dessin.trucks.camion import Camion
from utils.dashboard import Dashboard

# Initialiser Pygame
pygame.init()

# Configurer la fenêtre
taille_ecran = largeur, hauteur = 800, 600
ecran = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Simulation de Transport")

# Initialiser le module de police et créer un objet Font
pygame.font.init()
font = pygame.font.SysFont('arial', 20)

# Initialiser le camion avec la vitesse intégrée dans sa logique de déplacement
camion = Camion('images/truck_1.png', [0, 250], (120, 30), 5)  # Ajustez la vitesse selon les besoins

# Initialiser le dashboard pour l'affichage de la vitesse et des coordonnées
dashboard = Dashboard(font)

# Boucle de jeu
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        # Ajoutez ici la gestion des événements de drag si nécessaire

    # Mise à jour du camion en fonction de sa logique interne
    camion.mettre_a_jour(largeur)

    # Effacer l'écran
    ecran.fill((255, 255, 255))

    # Dessiner le camion
    camion.dessiner(ecran)

    # Afficher la vitesse et les coordonnées du camion
    dashboard.afficher_vitesse_et_coordonnees(ecran, camion.vitesse, camion.position)

    # Actualiser l'affichage
    pygame.display.flip()

    # Limiter les frames par seconde (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

import pygame
import sys
from dessin.trucks.camion import Camion  # Assurez-vous que votre classe Camion est mise à jour pour gérer le déplacement diagonal
from utils.dashboard import Dashboard
from utils.routes import Route

# Initialiser Pygame
pygame.init()

# Configurer la fenêtre
taille_ecran = largeur, hauteur = 800, 600
ecran = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Simulation de Transport")

# Initialiser le module de police
pygame.font.init()
font = pygame.font.SysFont('arial', 20)

# Définir les points de départ et d'arrivée
point_depart = [50, 250]
point_arrivee = [700, 350]  # Changez ceci pour tester différents déplacements

# Initialiser le camion avec la position de départ
camion = Camion('images/truck_1.png', point_depart, (120, 30), 5)  # Ajustez la vitesse si nécessaire

# Ajouter la logique pour définir les points de départ et d'arrivée dans votre Camion
camion.definir_itineraire(point_depart, point_arrivee)

# Initialiser le dashboard
dashboard = Dashboard(font)

# Initialiser la route
route = Route(point_depart, point_arrivee)
# Boucle de jeu
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

    # Effacer l'écran
    ecran.fill((255, 255, 255))

    # Mise à jour et dessin du camion
    camion.mise_a_jour()
    camion.dessiner(ecran)

    # Dessiner la route
    route.dessiner(ecran)

    # Afficher la vitesse et les coordonnées du camion
    dashboard.afficher_vitesse_et_coordonnees(ecran, camion.vitesse, camion.position)

    # Actualiser l'affichage
    pygame.display.flip()

    # Limiter les frames par seconde (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

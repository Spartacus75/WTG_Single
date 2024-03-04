import pygame
import sys
from dessin.eolienne_components.tour import dessiner_section_tour
from dessin.trucks.truck import dessiner_camion


# Initialisation de Pygame
pygame.init()

# Définition des dimensions de l'écran
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# Couleurs
black = (0, 0, 0)

# Boucle principale
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Remplit l'écran avec la couleur de fond
	screen.fill(black)


	# Dessine les quatre sections de tour
	dessiner_section_tour(screen, 100, 100, 75, 25)  # Exemple de dimensions et position
	dessiner_section_tour(screen, 200, 100, 75, 25)  # Modifiez ces valeurs selon vos besoins
	dessiner_section_tour(screen, 300, 100, 75, 25)
	dessiner_section_tour(screen, 400, 100, 75, 25)

	#Dessin camion
	dessiner_camion(screen, 500, 100, 50, 12)
	dessiner_camion(screen, 700, 100, 50, 12)


	# Met à jour l'affichage
	pygame.display.flip()

pygame.quit()
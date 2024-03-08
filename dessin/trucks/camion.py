import pygame

class Camion:
    def __init__(self, image_path, position, taille, vitesse):
        self.image_originale = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image_originale, taille)
        self.position = list(position)
        self.taille = taille
        self.vitesse = vitesse
        self.direction = "to_B"  # Initialiser la direction du camion

    def dessiner(self, ecran):
        ecran.blit(self.image, self.position)

    def mettre_a_jour_position(self, deplacement_x, deplacement_y):
        self.position[0] += deplacement_x
        self.position[1] += deplacement_y

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def mettre_a_jour(self, largeur_ecran):
        # Mise à jour basée sur la direction actuelle
        if self.direction == "to_B":
            self.position[0] += self.vitesse
            if self.position[0] + self.taille[0] >= largeur_ecran:  # Si le camion atteint le côté droit
                self.direction = "to_A"
                self.flip()
        elif self.direction == "to_A":
            self.position[0] -= self.vitesse
            if self.position[0] <= 0:  # Si le camion atteint le côté gauche
                self.direction = "to_B"
                self.flip()

import pygame
import math

class Camion:
    def __init__(self, image_path, position, taille, vitesse):
        # Chargement et redimensionnement de l'image du camion
        self.image_originale = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image_originale, taille)
        # Initialisation de la position et de la vitesse
        self.position = list(position)
        self.taille = taille
        self.vitesse = vitesse
        # Direction initiale et état de mouvement
        self.direction_to_arrivee = True
        self.en_mouvement = True
        # Points de départ et d'arrivée non définis initialement
        self.point_depart = None
        self.point_arrivee = None
        self.destination_actuelle = None

    def dessiner(self, ecran):
        # Affiche le camion à sa position actuelle sur l'écran
        ecran.blit(self.image, self.position)

    def definir_itineraire(self, depart, arrivee):
        # Définit les points de départ et d'arrivée et la destination actuelle
        self.point_depart = depart
        self.point_arrivee = arrivee
        self.destination_actuelle = self.point_arrivee

    def mise_a_jour(self):
        if not self.en_mouvement or self.destination_actuelle is None:
            return  # Ne pas bouger si le camion est à l'arrêt ou si aucun itinéraire n'est défini

        # Calcul de la direction vers la destination actuelle
        dx = self.destination_actuelle[0] - self.position[0]
        dy = self.destination_actuelle[1] - self.position[1]
        distance = math.hypot(dx, dy)

        if distance < self.vitesse:
            # Le camion est arrivé à sa destination
            self.position = self.destination_actuelle[:]
            if self.destination_actuelle == self.point_arrivee:
                self.destination_actuelle = self.point_depart  # Changer la destination pour revenir
                self.flip()
            else:
                self.destination_actuelle = self.point_arrivee
                self.en_mouvement = False  # S'arrêter à l'arrivée
            return

        # Mouvement vers la destination
        dx /= distance
        dy /= distance
        self.position[0] += dx * self.vitesse
        self.position[1] += dy * self.vitesse

    def demarrer(self):
        # Permet de redémarrer le mouvement du camion après un arrêt
        self.en_mouvement = True
        # Définit la destination actuelle selon la position du camion
        if self.position == self.point_depart:
            self.destination_actuelle = self.point_arrivee
        elif self.position == self.point_arrivee:
            self.destination_actuelle = self.point_depart
        else:
            # Si le camion est entre les deux points, il continue vers sa destination actuelle
            pass

    def flip(self):
        # Retourne l'image du camion si nécessaire
        self.image = pygame.transform.flip(self.image, True, False)

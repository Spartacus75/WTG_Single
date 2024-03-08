import pygame

class Route:
    def __init__(self, point_depart, point_arrivee, couleur=(0, 0, 0), epaisseur=5):
        self.point_depart = point_depart
        self.point_arrivee = point_arrivee
        self.couleur = couleur
        self.epaisseur = epaisseur

    def dessiner(self, ecran):
        pygame.draw.line(ecran, self.couleur, self.point_depart, self.point_arrivee, self.epaisseur)

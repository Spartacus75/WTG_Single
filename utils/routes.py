import pygame

class Route:
    def __init__(self, point_depart, point_arrivee, couleur=(0, 0, 0), epaisseur=5):
        self.point_depart = point_depart
        self.point_arrivee = point_arrivee
        self.couleur = couleur
        self.epaisseur = epaisseur

    def dessiner(self, ecran, offset_x=0, offset_y=0):
        # Applique l'offset aux points de départ et d'arrivée
        point_depart_avec_offset = (self.point_depart[0] + offset_x, self.point_depart[1] + offset_y)
        point_arrivee_avec_offset = (self.point_arrivee[0] + offset_x, self.point_arrivee[1] + offset_y)
        
        # Dessine la route avec les points ajustés
        pygame.draw.line(ecran, self.couleur, point_depart_avec_offset, point_arrivee_avec_offset, self.epaisseur)
import pygame

class Dashboard:
    def __init__(self, font):
        self.font = font

    def afficher_vitesse_et_coordonnees(self, ecran, vitesse, position_camion):
        # Afficher la vitesse
        texte_vitesse = self.font.render(f'Vitesse: {vitesse} pixels/frame', True, (0, 0, 0))
        ecran.blit(texte_vitesse, (10, 10))
        
        # Afficher les coordonnées du camion
        texte_coordonnees = self.font.render(f'Coordonnées: X={position_camion[0]}, Y={position_camion[1]}', True, (0, 0, 0))
        ecran.blit(texte_coordonnees, (10, 35))

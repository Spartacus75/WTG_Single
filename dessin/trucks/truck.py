import pygame

def dessiner_camion(screen, x, y, width=60, height=30, color=(0, 128, 255)):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
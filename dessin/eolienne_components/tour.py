import pygame

def dessiner_section_tour(screen, x, y, width, height, color=(255, 255, 255)):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))

import pygame

class Camera:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0
        self.drag_start = None

    def start_drag(self, pos):
        self.drag_start = pos

    def update_drag(self, pos):
        if self.drag_start:
            dx = pos[0] - self.drag_start[0]
            dy = pos[1] - self.drag_start[1]
            self.offset_x += dx
            self.offset_y += dy
            self.drag_start = pos

    def stop_drag(self):
        self.drag_start = None

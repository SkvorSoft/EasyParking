import pygame


# Klasse mit Parkplätzen (Koordinaten, Größen, Farbe)
class PP_Ort:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.hohe = 64
        self.breite = 32
        self.window = window
        self.color = (255, 255, 255)

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.breite, self.hohe), 3)

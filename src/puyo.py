import pygame

class Puyo:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen, x_offset=0, y_offset=0):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x + x_offset, self.y + y_offset),
            10
        )

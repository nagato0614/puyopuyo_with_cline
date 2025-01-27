import pygame
from src.constant import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR, FPS
from src.field import Field
from src.puyopair import PuyoPair
from src.nextpuyo import NextPuyo

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Puyo Puyo")
        self.clock = pygame.time.Clock()
        self.field = Field()
        self.falling_puyo = PuyoPair()
        self.next_puyo = NextPuyo()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BACKGROUND_COLOR)
            self.field.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

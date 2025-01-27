import pygame
from src.game import Game
from src.constant import WINDOW_WIDTH, WINDOW_HEIGHT

def main():
    pygame.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

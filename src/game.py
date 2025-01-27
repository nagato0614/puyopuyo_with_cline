import pygame
from src.field import Field
from src.puyopair import PuyoPair
from src.nextpuyo import NextPuyo

class Game:
    def __init__(self):
        self.field = Field()
        self.falling_puyo = PuyoPair()
        self.next_puyo = NextPuyo()

    def run(self):
        # ゲームのメインループをここに実装
        pass

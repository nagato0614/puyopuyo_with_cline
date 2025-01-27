import random
from src.constant import PUYO_COLORS
from src.puyo import Puyo

class PuyoPair:
    def __init__(self):
        colors = list(PUYO_COLORS.keys())
        self.puyo_main = Puyo(random.choice(colors))
        self.puyo_sub = Puyo(random.choice(colors))
        self.x = 0
        self.y = 0
        self.rotation_state = 'UP'

    def draw(self):
        # ぷよペアを描画する処理をここに実装
        pass

    def rotate(self, direction):
        # ぷよペアを回転させる処理をここに実装
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

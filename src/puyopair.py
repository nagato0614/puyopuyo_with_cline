import random
from src.constant import PUYO_COLORS
from src.puyo import Puyo

class PuyoPair:
    def __init__(self, screen=None, puyo_field=None):
        colors = list(PUYO_COLORS.keys())
        self.puyo_main = Puyo(x=0, y=0, color=random.choice(colors))
        self.puyo_sub = Puyo(x=0, y=0, color=random.choice(colors))
        self.x = 0
        self.y = 0
        self.rotation_state = 'UP'

    def draw(self):
        # ぷよペアを描画する処理をここに実装
        pass

    def rotate(self, direction):
        if direction == 'CLOCKWISE':
            self.rotation_state = {'UP': 'RIGHT', 'RIGHT': 'DOWN', 'DOWN': 'LEFT', 'LEFT': 'UP'}[self.rotation_state]
        elif direction == 'COUNTER_CLOCKWISE':
            self.rotation_state = {'UP': 'LEFT', 'LEFT': 'DOWN', 'DOWN': 'RIGHT', 'RIGHT': 'UP'}[self.rotation_state]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

from src.puyo import Puyo
import random
from src.constant import PUYO_COLORS

class NextPuyo:
    def __init__(self):
        self.puyo_main = Puyo(random.choice(list(PUYO_COLORS.keys())))
        self.puyo_sub = Puyo(random.choice(list(PUYO_COLORS.keys())))

    def draw(self):
        # 次のぷよペアを描画する処理をここに実装
        pass

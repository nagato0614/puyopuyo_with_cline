class Field:
    def __init__(self):
        self.field = [[None for _ in range(6)] for _ in range(14)]

    def draw(self):
        # フィールドを描画する処理をここに実装
        pass

    def set_puyo(self, x, y, puyo):
        self.field[y][x] = puyo

    def is_settable(self, x, y):
        return self.field[y][x] is None

    def delete_connected_puyo(self):
        # 連結しているぷよを消去する処理をここに実装
        pass

    def apply_gravity(self):
        # 上のぷよを落下させる処理をここに実装
        pass

    def check_game_over(self):
        # ゲームオーバー判定をここに実装
        pass

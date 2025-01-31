import pygame
from src.constant import GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, BOARD_MARGIN, BORDER_WIDTH, BACKGROUND_COLOR, GRID_COLOR, BORDER_COLOR, GUIDE_LINE_COLOR

class Field:
    def __init__(self):
        self.field = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def draw(self, screen):
          # 背景をクリア
        screen.fill(BACKGROUND_COLOR)

          # 盤面のグリッド描画
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(
                    x * CELL_SIZE + BOARD_MARGIN,
                    y * CELL_SIZE + BOARD_MARGIN,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)

          # ボーダー描画
        border_rect = pygame.Rect(
            BOARD_MARGIN - BORDER_WIDTH,
            BOARD_MARGIN - BORDER_WIDTH,
            (GRID_WIDTH * CELL_SIZE) + 2 * BORDER_WIDTH,
            (GRID_HEIGHT * CELL_SIZE) + 2 * BORDER_WIDTH
        )
        pygame.draw.rect(screen, BORDER_COLOR, border_rect)

          # ガイドライン描画（中心線）
        center_x = (GRID_WIDTH * CELL_SIZE) // 2 + BOARD_MARGIN
        center_y = (GRID_HEIGHT * CELL_SIZE) // 2 + BOARD_MARGIN
        pygame.draw.line(
            screen,
            GUIDE_LINE_COLOR,
            (center_x, BOARD_MARGIN),
            (center_x, GRID_HEIGHT * CELL_SIZE + BOARD_MARGIN),
            1
        )
        pygame.draw.line(
            screen,
            GUIDE_LINE_COLOR,
            (BOARD_MARGIN, center_y),
            (GRID_WIDTH * CELL_SIZE + BOARD_MARGIN, center_y),
            1
        )

    def set_puyo(self, x, y, puyo): 
           # 位置(x,y)にぷよを設置
        if self.is_settable(x, y):
            self.field[y][x] = puyo
            return True
        return False

    def is_settable(self, x, y):
        return self.field[y][x] is None

    def delete_connected_puyo(self):
         # 連結しているぷよを消去する処理をここに実装
        pass

    def get_puyo(self, x, y):
        return self.field[y][x]

    def apply_gravity(self):
        # 上のぷよを落下させる処理をここに実装
        pass

    def check_game_over(self):
        # ゲームオーバー判定をここに実装
        pass

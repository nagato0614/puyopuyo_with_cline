# constant.py

# 定数の定義
PI = 3.14159
E = 2.71828
SPEED_OF_LIGHT = 299792458  # m/s
GRAVITY = 9.80665  # m/s^2

# ぷよぷよゲームの定数
WIDTH = 800  # ウィンドウの幅
HEIGHT = 600  # ウィンドウの高さ
FPS = 60  # ゲームのFPS
CELL_WIDTH = 40  # フィールドのマスの幅
CELL_HEIGHT = 40  # フィールドのマスの高さ
FIELD_WIDTH = 6  # フィールドの幅（マス数）
FIELD_HEIGHT = 14  # フィールドの高さ（マス数）
PUYO_COLORS = {
    'RED': '#FF0000',
    'GREEN': '#00FF00',
    'BLUE': '#0000FF',
    'YELLOW': '#FFFF00'
}
PUYO_FALL_SPEED = 1.0  # ぷよの落下速度
PUYO_FAST_FALL_SPEED = 2.0  # ぷよの落下速度（高速）
PUYO_LOSE_Y = 12  # ゲームオーバーとなるぷよのY座標
PUYO_ROTATE_STATE = {
    'UP': 'UP',
    'RIGHT': 'RIGHT',
    'DOWN': 'DOWN',
    'LEFT': 'LEFT'
}
KEY_LEFT = '←'  # 左キー
KEY_RIGHT = '→'  # 右キー
KEY_DOWN = '↓'  # 下キー
KEY_Z = 'z'  # Zキー
KEY_X = 'x'  # Xキー

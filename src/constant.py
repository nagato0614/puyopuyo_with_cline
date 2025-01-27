# Puyo Puyo Game Constants
# Grid dimensions (cells)
GRID_WIDTH = 6
GRID_HEIGHT = 12

# Cell size in pixels
CELL_SIZE = 40

# Board margins and border
BOARD_MARGIN = 50
BORDER_WIDTH = 3

# Window dimensions
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE + 2 * BOARD_MARGIN
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + 2 * BOARD_MARGIN

# Colors
BACKGROUND_COLOR = (240, 230, 200)   # Beige
GRID_COLOR = (169, 169, 169)         # Dark Gray
BORDER_COLOR = (100, 100, 100)       # Medium Gray
GUIDE_LINE_COLOR = (255, 0, 0)        # Red

# Puyo colors (to be used in other components)
PUYO_COLORS = {
    'RED': (255, 0, 0),
    'BLUE': (0, 0, 255),
    'GREEN': (0, 255, 0),
    'YELLOW': (255, 255, 0),
    'PURPLE': (147, 51, 255),
    'CYAN': (0, 255, 255)
}

# Frames per second
FPS = 60

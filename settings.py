import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100

# map settings
MAP_SCALE = 7
MAP_DEPTH = 100

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS

DISTANCE = NUM_RAYS / (2 * math.tan(HALF_FOV))
SCALE = WIDTH / NUM_RAYS
PROJ_COEFF = 3 * DISTANCE * TILE

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY = (30, 30, 235)
DARK_GRAY = (120, 120, 120)
SALMON = (255, 160, 122)

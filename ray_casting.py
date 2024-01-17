import math
import pygame
import settings as st
from map import world_map


def ray_casting(sc, player_position, player_angle):
    cur_angle = player_angle - st.HALF_FOV
    xo, yo = player_position
    for ray in range(st.NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(st.MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            if (x // st.TILE * st.TILE, y // st.TILE * st.TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = st.PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(sc, color,
                                 (ray * st.SCALE, st.HALF_HEIGHT - proj_height // 2, st.SCALE, proj_height))
                break
        for depth_m in range(st.MAP_DEPTH):
            x1 = xo + depth_m * cos_a
            y1 = yo + depth_m * sin_a
            if (x1 // st.TILE * st.TILE, y1 // st.TILE * st.TILE) in world_map:
                break
        pygame.draw.line(sc, st.DARK_GRAY, (player_position[0]//st.MAP_SCALE, player_position[1]//st.MAP_SCALE),
                         (x1//st.MAP_SCALE, y1//st.MAP_SCALE), 1)

        cur_angle += st.DELTA_ANGLE
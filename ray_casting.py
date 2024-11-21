import math
import pygame
import settings as st
from map import world_map

def mapping(a, b):
    return (a // st.TILE)* st.TILE, (b // st.TILE)* st.TILE

def ray_casting(sc, player_position, player_angle):
    xo, yo = player_position
    xm, ym = mapping(xo, yo)
    cur_angle = player_angle - st.HALF_FOV
    for ray in range(st.NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # vertical
        x, dx = (xm + st.TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, st.WIDTH, st.TILE):
            depth_v = (x-xo) / cos_a
            y = yo + depth_v * sin_a
            if mapping(x+dx, y) in world_map:
                break
            x += dx * st.TILE

        # horizontal
        y, dy = (ym + st.TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, st.HEIGHT, st.TILE):
            depth_h = (y - yo) / sin_a
            x = xo + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * st.TILE

        # projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.0000001)
        proj_height = min(int(st.PROJ_COEFF / depth), 2 * st.HEIGHT)
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c // 2, c // 3)
        pygame.draw.rect(sc, color,(ray * st.SCALE, st.HALF_HEIGHT - proj_height // 2, st.SCALE, proj_height))
        cur_angle += st.DELTA_ANGLE


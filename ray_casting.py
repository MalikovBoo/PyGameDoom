import math
import pygame
import settings as st
from map import world_map

def mapping(a, b):
    return (a // st.TILE)* st.TILE, (b // st.TILE)* st.TILE

def ray_casting(sc, player_position, player_angle, textures):
    xo, yo = player_position
    xm, ym = mapping(xo, yo)
    cur_angle = player_angle - st.HALF_FOV
    texture_v = '1'
    texture_h = '1'
    for ray in range(st.NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # vertical
        x, dx = (xm + st.TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, st.WIDTH, st.TILE):
            depth_v = (x-xo) / cos_a
            yv = yo + depth_v * sin_a
            tile_v = mapping(x+dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * st.TILE

        # horizontal
        y, dy = (ym + st.TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, st.HEIGHT, st.TILE):
            depth_h = (y - yo) / sin_a
            xh = xo + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * st.TILE

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % st.TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.0000001)
        proj_height = min(int(st.PROJ_COEFF / depth), 2 * st.HEIGHT)

        wall_column = textures[texture].subsurface(offset * st.TEXTURE_SCALE, 0, st.TEXTURE_SCALE, st.TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (st.SCALE, proj_height))

        sc.blit(wall_column, (ray * st.SCALE, st.HALF_HEIGHT - proj_height // 2))

        cur_angle += st.DELTA_ANGLE


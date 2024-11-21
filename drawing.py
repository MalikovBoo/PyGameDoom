import pygame
import math
import settings as st
from ray_casting import ray_casting
from map import world_map, mini_map
from settings import MAP_TILE


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.sc, st.SKY, (0, 0, st.WIDTH, st.HALF_HEIGHT))
        pygame.draw.rect(self.sc, st.DARK_GRAY, (0, st.HALF_HEIGHT, st.WIDTH, st.HEIGHT))

    def world(self, pos, angle):
        ray_casting(self.sc, pos, angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, st.RED)
        self.sc.blit(render, st.FPS_POS)

    def minimap(self, player):
        self.sc_map.fill(st.BLACK)
        map_x, map_y = player.x // st.MAP_SCALE, player.y // st.MAP_SCALE
        pygame.draw.line(self.sc_map, st.YELLOW, (map_x, map_y), (map_x+12 * math.cos(player.angle), map_y+12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, st.SALMON, (int(map_x), int(map_y)), 4)

        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, st.GREEN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, st.MAP_POS)

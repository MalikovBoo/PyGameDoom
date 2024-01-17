import pygame
import settings as st
from player import Player
import math
from map import world_map
from ray_casting import ray_casting


def game_start():
    pygame.init()
    sc = pygame.display.set_mode((st.WIDTH, st.HEIGHT))
    clock = pygame.time.Clock()
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        sc.fill(st.BLACK)
        player.movement()

        pygame.draw.rect(sc, st.SKY, (0, 0, st.WIDTH, st.HALF_HEIGHT))
        pygame.draw.rect(sc, st.DARK_GRAY, (0, st.HALF_HEIGHT, st.WIDTH, st.HEIGHT))
        for x, y in world_map:
            pygame.draw.rect(sc, st.DARK_GRAY, (x//st.MAP_SCALE, y//st.MAP_SCALE,
                                                st.TILE//st.MAP_SCALE, st.TILE//st.MAP_SCALE))

        # pygame.draw.line(sc, st.DARK_GRAY, (player.pos[0]//st.MAP_SCALE, player.pos[1]//st.MAP_SCALE),
        #                  ((player.x + st.MAP_DEPTH * math.cos(player.angle))//st.MAP_SCALE,
        #                   (player.y + st.MAP_DEPTH * math.sin(player.angle))//st.MAP_SCALE),
        #                                                 1)
        ray_casting(sc, player.pos, player.angle)

        pygame.draw.circle(sc, st.SALMON, (player.pos[0]//st.MAP_SCALE, player.pos[1]//st.MAP_SCALE), 2)

        pygame.display.flip()
        clock.tick(st.FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_start()


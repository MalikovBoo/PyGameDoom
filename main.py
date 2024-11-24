import pygame
from Tools.scripts.findnocoding import decl_re
import settings as st
from player import Player
from drawing import Drawing


def game_start():
    pygame.init()
    sc = pygame.display.set_mode((st.WIDTH, st.HEIGHT))
    sc_map = pygame.Surface((st.WIDTH // st.MAP_SCALE, st.HEIGHT // st.MAP_SCALE))
    clock = pygame.time.Clock()
    player = Player()
    drawing = Drawing(sc, sc_map)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        sc.fill(st.BLACK)
        player.movement()

        drawing.background(player.angle)
        drawing.world(player.pos, player.angle)
        drawing.fps(clock)
        drawing.minimap(player)

        pygame.display.flip()
        clock.tick(st.FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_start()


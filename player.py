import settings as st
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = st.player_pos
        self.angle = st.player_angle

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += st.player_speed * cos_a
            self.y += st.player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -st.player_speed * cos_a
            self.y += -st.player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += st.player_speed * sin_a
            self.y += -st.player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -st.player_speed * sin_a
            self.y += st.player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

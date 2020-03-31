import pygame
from utility import white
from random import randint
from config import Config


class Ball:

    radius = 10

    def __init__(self, game):
        self.x = Config.field_width // 2
        self.y = Config.field_height // 2
        self.speed_x = randint(-5, 5)
        self.speed_y = randint(-5, 5)
        self.game = game

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.check_wall_hit()

    def draw(self, screen):
        pygame.draw.circle(screen, white, (self.x, self.y), Ball.radius, 0)

    def check_wall_hit(self):
        if self.x - Ball.radius <= 0:
            self.speed_x *= -1
            self.game.player_right.score += 1
        elif self.x + Ball.radius >= Config.field_width:
            self.speed_x *= -1
            self.game.player_left.score += 1
        if self.y - Ball.radius <= 0 or self.y + Ball.radius >= Config.field_height:
            self.speed_y *= -1

import pygame
from utility import white
from config import Config


class Player:

    left = 0
    right = 1

    def __init__(self, player_pos, game):
        self.y = Config.field_height // 2
        self.pos = player_pos  # right or left side
        self.game = game
        if self.pos == Player.left:
            self.x = Config.player_width // 2
        else:
            self.x = Config.field_width - Config.player_width // 2

        self.speed_y = 0
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, white, (self.x - Config.player_width // 2, self.y - Config.player_height // 2,
                                         Config.player_width, Config.player_height), 0)
        # draw the player paddle

    def update(self):
        self.y += self.speed_y
        self.check_bounds()

    def check_bounds(self):
        if self.y - Config.player_height // 2 < 0:
            self.y = Config.player_height // 2
        elif self.y + Config.player_height // 2 > Config.field_height:
            self.y = Config.field_height - Config.player_height // 2

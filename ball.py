import pygame
from utility import white, get_dist
from random import randint
from config import Config
from math import sqrt


class Ball:

    def __init__(self, game):
        self.x = Config.field_width // 2
        self.y = Config.field_height // 2
        self.speed_x = randint(-3, 3)
        while self.speed_x == 0:
            self.speed_x = randint(-3, 3)
        self.speed_y = 0
        self.game = game

    def reset(self):
        self.x = Config.field_width // 2
        self.y = Config.field_height // 2
        self.speed_x = randint(-3, 3)
        while self.speed_x == 0:
            self.speed_x = randint(-3, 3)
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if not self.check_player_hit():
            self.check_wall_hit()

    def draw(self, screen):
        pygame.draw.circle(screen, white, (int(round(self.x)), int(round(self.y))), Config.ball_radius, 0)

    def check_wall_hit(self):
        if self.x - Config.ball_radius <= 0:
            self.speed_x *= -1
            self.game.player_right.score += 1
            self.reset()
        elif self.x + Config.ball_radius >= Config.field_width:
            self.speed_x *= -1
            self.game.player_left.score += 1
            self.reset()
        if self.y - Config.ball_radius <= 0 or self.y + Config.ball_radius >= Config.field_height:
            self.speed_y *= -1

    def check_player_hit(self):
        p1cx = self.game.player_left.x + Config.player_width // 2
        p1ucy = self.game.player_left.y - Config.player_height // 2
        p1lcy = self.game.player_left.y + Config.player_height // 2

        p2cx = self.game.player_right.x - Config.player_width // 2
        p2ucy = self.game.player_right.y - Config.player_height // 2
        p2lcy = self.game.player_right.y + Config.player_height // 2

        if self.x - Config.ball_radius <= p1cx:
            if p1ucy <= self.y <= p1lcy:
                self.speed_x *= -1
                self.x = p1cx + Config.ball_radius + 1

                speed = get_dist(0, 0, self.speed_x, self.speed_y)
                tan_a_speed = self.speed_y / self.speed_x
                cos_a_speed = self.speed_x / speed
                speed += abs(self.game.player_left.speed_y)
                self.speed_x = cos_a_speed * speed
                self.speed_y = tan_a_speed * self.speed_x

                return True
            elif self.y < p1ucy and get_dist(self.x, self.y, p1cx, p1ucy) <= Config.ball_radius:  # upper corner hit
                x = self.x - p1cx
                y = self.y - p1ucy
                c = -2*(self.speed_x*x + self.speed_y*y) / (x**2 + y**2)
                self.speed_x = (self.speed_x + c * x)
                self.speed_y = (self.speed_y + c * y)
                tan_a = abs(y) / abs(x)
                cos_a = abs(x) / get_dist(self.x, self.y, p1cx, p1ucy)
                self.x = p1cx + (Config.ball_radius+1) * cos_a
                self.y = p1ucy - tan_a * abs(self.x - p1cx)

                speed = get_dist(0, 0, self.speed_x, self.speed_y)
                tan_a_speed = self.speed_y / self.speed_x
                cos_a_speed = self.speed_x / speed
                speed += abs(self.game.player_left.speed_y)
                self.speed_x = cos_a_speed * speed
                self.speed_y = tan_a_speed * self.speed_x



                return True
            elif self.y > p1lcy and get_dist(self.x, self.y, p1cx, p1lcy) <= Config.ball_radius:  # lower corner hit
                x = self.x - p1cx
                y = self.y - p1lcy
                c = -2 * (self.speed_x * x + self.speed_y * y) / (x ** 2 + y ** 2)
                self.speed_x = (self.speed_x + c * x)
                self.speed_y = (self.speed_y + c * y)
                tan_a = abs(y) / abs(x)
                cos_a = abs(x) / get_dist(self.x, self.y, p1cx, p1lcy)
                self.x = p1cx + (Config.ball_radius + 1) * cos_a
                self.y = p1lcy + tan_a * abs(self.x - p1cx)

                speed = get_dist(0, 0, self.speed_x, self.speed_y)
                tan_a_speed = self.speed_y / self.speed_x
                cos_a_speed = self.speed_x / speed
                speed += abs(self.game.player_left.speed_y)
                self.speed_x = cos_a_speed * speed
                self.speed_y = tan_a_speed * self.speed_x


                return True
        elif self.x + Config.ball_radius >= p2cx:
            if p2ucy <= self.y <= p2lcy:
                self.speed_x *= -1
                self.x = p2cx - Config.ball_radius - 1

                speed = get_dist(0, 0, self.speed_x, self.speed_y)
                tan_a_speed = self.speed_y / self.speed_x
                cos_a_speed = self.speed_x / speed
                speed += abs(self.game.player_left.speed_y)
                self.speed_x = cos_a_speed * speed
                self.speed_y = tan_a_speed * self.speed_x


                return True
            elif self.y < p2ucy and get_dist(self.x, self.y, p2cx, p2ucy) <= Config.ball_radius:
                x = self.x - p2cx
                y = self.y - p2ucy
                c = -2*(self.speed_x*x + self.speed_y*y) / (x**2 + y**2)
                self.speed_x = (self.speed_x + c * x)
                self.speed_y = (self.speed_y + c * y)
                tan_a = abs(y) / abs(x)
                cos_a = abs(x) / get_dist(self.x, self.y, p2cx, p2ucy)
                self.x = p2cx - (Config.ball_radius + 1) * cos_a
                self.y = p2ucy - tan_a * abs(self.x - p2cx)

                speed = get_dist(0, 0, self.speed_x, self.speed_y)
                tan_a_speed = self.speed_y / self.speed_x
                cos_a_speed = self.speed_x / speed
                speed += abs(self.game.player_left.speed_y)
                self.speed_x = cos_a_speed * speed
                self.speed_y = tan_a_speed * self.speed_x

                return True
            elif self.y > p2lcy and get_dist(self.x, self.y, p2cx, p2lcy) <= Config.ball_radius:
                x = self.x - p2cx
                y = self.y - p2lcy
                c = -2 * (self.speed_x * x + self.speed_y * y) / (x ** 2 + y ** 2)
                self.speed_x = (self.speed_x + c * x)
                self.speed_y = (self.speed_y + c * y)
                tan_a = abs(y) / abs(x)
                cos_a = abs(x) / get_dist(self.x, self.y, p2cx, p2lcy)
                self.x = p2cx - (Config.ball_radius + 1) * cos_a
                self.y = p2lcy + tan_a * abs(self.x - p2cx)

                speed = get_dist(0, 0, self.speed_x, self.speed_y)
                tan_a_speed = self.speed_y / self.speed_x
                cos_a_speed = self.speed_x / speed
                speed += abs(self.game.player_left.speed_y)
                self.speed_x = cos_a_speed * speed
                self.speed_y = tan_a_speed * self.speed_x

                return True
        else:
            return False

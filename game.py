from player import Player
from ball import Ball


class Game:

    game_over_text_color = (0, 255, 0)
    game_over_text_size = 45
    game_over_text_font = "Arial"
    over = False

    def __init__(self):
        self.player_left = Player(Player.left, self)
        self.player_right = Player(Player.right, self)
        self.ball = Ball(self)

    def update_all(self):
        self.player_left.update()
        self.player_right.update()
        self.ball.update()

    def draw_all(self, screen):
        self.player_right.draw(screen)
        self.player_left.draw(screen)
        self.ball.draw(screen)





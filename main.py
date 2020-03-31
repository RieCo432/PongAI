from game import Game
import pygame
from player import Player
import sys
from os import environ
from utility import black
from config import Config
from datetime import datetime

if __name__ == "__main__":

    num_games = 1
    games = []
    for i in range(num_games):
        games.append(Game())
    active_game = 0
    draw_all = False

    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
    pygame.init()
    screen = pygame.display.set_mode((Config.field_width, Config.field_height))
    pygame.font.init()
    myfont = pygame.font.SysFont(Game.game_over_text_font, Game.game_over_text_size)
    screen.fill(0)
    frameend = datetime.now()
    frametimes = [0.001] * 101
    last_framerate_update = datetime.now()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    games[active_game].player_left.speed_y = - Config.player_speed
                elif event.key == pygame.K_s:
                    games[active_game].player_left.speed_y = Config.player_speed
                if event.key == pygame.K_UP:
                    games[active_game].player_right.speed_y = - Config.player_speed
                elif event.key == pygame.K_DOWN:
                    games[active_game].player_right.speed_y = Config.player_speed
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    games[active_game].player_left.speed_y = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    games[active_game].player_right.speed_y = 0

        screen.fill(black)
        for game in games:
            game.update_all()
            if draw_all:
                game.draw_all(screen)
        if not draw_all:
            games[active_game].draw_all(screen)

        pygame.display.update()
        if len(frametimes) > 100:
            frametimes = frametimes[-100:-1]

        frametimes.append((datetime.now() - frameend).total_seconds())
        frameend = datetime.now()
        if (datetime.now() - last_framerate_update).total_seconds() > 0.5:
            pygame.display.set_caption("%f player 1: %d player 2: %d" % (1/(sum(frametimes)/len(frametimes)),
                                                                         games[active_game].player_left.score,
                                                                         games[active_game].player_right.score))
            last_framerate_update = datetime.now()

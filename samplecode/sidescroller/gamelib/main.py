import pygame

from settings import SCREEN_SIZE
from game import Game

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # create game
    game = Game(screen)
    try:
        game.run()
    except KeyboardInterrupt:
        game.quit()

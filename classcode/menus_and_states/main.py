import pygame

from app import Application
from 

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 800))

    # create game
    game = Game(screen)
    try:
        game.run()
    except KeyboardInterrupt:
        game.quit()

if __name__ == "__main__":
    main()

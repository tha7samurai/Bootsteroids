import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    ship = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        ship.draw(screen)
        pygame.display.flip()
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

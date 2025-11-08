print("DEBUG: reached top of main.py")
import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from AsteroidField import *
from shot import Shot
from logger import log_state, log_event

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    ship = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    AstField = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for a in asteroids:
            if ship.collides_with(a):
                log_event('player_hit')
                print('Game Over')
                sys.exit()
        screen.fill('black')
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()

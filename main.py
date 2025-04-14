import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # player.update(dt)
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        # player.draw(screen)
        for object in asteroids:
            if object.collisions(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()

        # Limit framerate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

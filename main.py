import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from pew import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    # Initial position for the player
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2

    # Sprite Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        for obj in asteroids:
            if obj.collisions(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collisions(asteroid):
                    bullet.kill()
                    asteroid.split()

        updatable.update(dt)
        pygame.display.flip()

        # Limit framerate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

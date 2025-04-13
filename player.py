import pygame
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Define the ship's layout
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Create the ship
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Define rotation speed
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # keys a and d make ship spin around
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    # keys w and s move ship forward and backward
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

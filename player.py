import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initialize the player with position, rotation, and radius.

        :param x: The initial x-coordinate of the player.
        :param y: The initial y-coordinate of the player.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Player's rotation angle in degrees

    def draw(self, screen):
        """
        Draw the player's triangle on the screen.

        :param screen: The Pygame surface on which the player is drawn.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        """
        Calculate the vertices of the player's triangle based on rotation.

        :return: A list of 3 Pygame Vector2 points forming the triangle's vertices.
        """
        forward = pygame.Vector2(0, -1).rotate(self.rotation)  # Forward direction
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5

        # Calculate triangle vertices
        a = self.position + forward * self.radius  # Front vertex
        b = self.position - forward * self.radius - right  # Rear left vertex
        c = self.position - forward * self.radius + right  # Rear right vertex

        return [a, b, c]

    def update(self, dt):
        """
        Update the player's state based on keyboard input.

        :param dt: Delta time (elapsed time since the last frame in seconds).
        """
        keys = pygame.key.get_pressed()

        # Handle forward and backward movement
        if keys[pygame.K_w]:
            self.move(-dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(dt)  # Move backward

        # Handle rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate counterclockwise
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate clockwise

    def rotate(self, dt):
        """
        Rotate the player by a speed scaled by delta time.

        :param dt: Delta time (elapsed time since the last frame in seconds).
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """
        Move the player in the direction of its rotation.

        :param dt: Delta time (elapsed time since the last frame in seconds).
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Forward direction
        self.position += forward * PLAYER_SPEED * dt

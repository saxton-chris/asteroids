from circleshape import CircleShape
from constants import *
import pygame
from typing import List, Tuple

class Player(CircleShape):
    """
    The Player class extends CircleShape to define a player object in the game.
    """

    DEFAULT_COLOR = "white"
    DEFAULT_LINE_WIDTH = 2

    def __init__(self, x: float, y: float, radius: float = PLAYER_RADIUS, containers=None):
        """
        Initialize the Player object.

        :param x: Initial x-coordinate of the player.
        :param y: Initial y-coordinate of the player.
        :param radius: Radius of the player, default value is PLAYER_RADIUS (assumed constant).
        :param containers: Optional parameter for managing the player in various containers.
        """
        super().__init__(x, y, radius)
        self.rotation: float = 0  # Player's rotation angle in degrees

        # Ensure the position is a pygame.Vector2 object
        self.position = pygame.Vector2(x, y)

    def triangle(self) -> Tuple[pygame.Vector2, pygame.Vector2, pygame.Vector2]:
        """
        Calculate the vertices of a triangle representing the player.

        :return: A tuple of 3 pygame.Vector2 points forming the triangle's vertices.
        """
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * (self.radius / 1.5)

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return (a, b, c)  # Returning a tuple for immutability

    def draw(self, screen: pygame.Surface, color: str = DEFAULT_COLOR, width: int = DEFAULT_LINE_WIDTH):
        """
        Draw the player as a triangle on the given screen.

        :param screen: The pygame surface on which the player is drawn.
        :param color: The color of the triangle, default is white.
        :param width: Line width of the triangle's edges, default is 2.
        """
        tri_points = self.triangle()
        pygame.draw.polygon(surface=screen, color=color, width=width, points=tri_points)

    def rotate(self, dt: float):
        """
        Rotates the player based on the given delta time.

        :param dt: Delta time (time elapsed since the last frame, in seconds).
                This ensures the rotation speed is frame-rate independent.
        """
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt: float):
        """
        Updates the player's state, including handling input for rotation and movement.

        :param dt: Delta time (time elapsed since the last frame, in seconds).
                This ensures frame-independent player actions.
        """
        keys = pygame.key.get_pressed()  # Get the current state of all keyboard keys

        # Handle rotation
        if keys[pygame.K_a]:  # Rotate counterclockwise
            self.rotate(-dt)
        if keys[pygame.K_d]:  # Rotate clockwise
            self.rotate(dt)

        # Handle movement
        if keys[pygame.K_w]:  # Move forward
            self.move(forward=True, dt=dt)
        if keys[pygame.K_s]:  # Move backward
            self.move(forward=False, dt=dt)


    def move(self, forward: bool, dt: float):
        """
        Moves the player in the current direction or opposite direction.

        :param forward: True to move forward, False to move backward.
        :param dt: Delta time (time elapsed since the last frame, in seconds).
                This ensures the movement speed is frame-rate independent.
        """
        # Determine the movement direction based on `forward`
        direction = -1 if forward else 1
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)  # Calculate forward direction
        self.position += direction * forward_vector * PLAYER_SPEED * dt  # Update position

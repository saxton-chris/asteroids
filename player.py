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

from circleshape import CircleShape  # Importing a custom CircleShape class
from constants import *  # Importing constants from a constants module
import pygame  # Importing pygame for vector operations and rendering


class Player(CircleShape):
    """
    The Player class extends CircleShape to define a player object in the game.
    """

    def __init__(self, x, y, radius=PLAYER_RADIUS, containers=None):
        """
        Initialize the Player object.

        :param x: Initial x-coordinate of the player.
        :param y: Initial y-coordinate of the player.
        :param radius: Radius of the player, default value is PLAYER_RADIUS (assumed constant).
        :param containers: Optional parameter for managing the player in various containers.
        """
        super().__init__(x, y, radius)  # Initialize the base CircleShape with position and radius
        self.rotation = 0  # Player's rotation angle in degrees

    def triangle(self):
        """
        Calculate the vertices of a triangle representing the player.

        The triangle points are determined based on the player's position, radius, and rotation.

        :return: A list of 3 pygame.Vector2 points forming the triangle's vertices.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Forward vector based on rotation
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5  # Perpendicular vector for width
        a = self.position + forward * self.radius  # Vertex at the front of the triangle
        b = self.position - forward * self.radius - right  # Left rear vertex
        c = self.position - forward * self.radius + right  # Right rear vertex
        return [a, b, c]  # Return the vertices as a list
    
    def draw(self, screen):
        """
        Draw the player as a triangle on the given screen.

        :param screen: The pygame surface on which the player is drawn.
        """
        tri_points = self.triangle()  # Get the triangle's vertices
        pygame.draw.polygon(
            surface=screen,  # The surface to draw on
            color="white",  # Color of the triangle
            width=2,  # Line width of the polygon
            points=tri_points  # The vertices of the triangle
        )
